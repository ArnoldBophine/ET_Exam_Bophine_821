"""
Synthetic Dataset Generator for DSA 2040A ETL Exam
Generates realistic e-commerce/retail transaction data
"""

import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta
import os

# Initialize Faker
fake = Faker()
Faker.seed(42)  # For reproducible results
np.random.seed(42)
random.seed(42)

def generate_synthetic_data(num_rows=10000):
    """
    Generate synthetic e-commerce transaction data
    
    Args:
        num_rows (int): Number of rows to generate
    
    Returns:
        pandas.DataFrame: Generated dataset
    """
    
    # Define realistic product categories and products
    categories = [
        'Electronics', 'Clothing', 'Home & Garden', 'Sports & Outdoors',
        'Books', 'Health & Beauty', 'Toys & Games', 'Automotive',
        'Food & Beverages', 'Office Supplies'
    ]
    
    products_by_category = {
        'Electronics': ['Smartphone', 'Laptop', 'Tablet', 'Headphones', 'Smart Watch', 'Camera', 'TV', 'Gaming Console'],
        'Clothing': ['T-Shirt', 'Jeans', 'Dress', 'Jacket', 'Shoes', 'Hat', 'Sweater', 'Shorts'],
        'Home & Garden': ['Sofa', 'Table', 'Chair', 'Lamp', 'Curtains', 'Plant Pot', 'Kitchen Set', 'Bedding'],
        'Sports & Outdoors': ['Running Shoes', 'Yoga Mat', 'Bicycle', 'Tennis Racket', 'Backpack', 'Water Bottle', 'Gym Equipment'],
        'Books': ['Fiction Novel', 'Textbook', 'Cookbook', 'Biography', 'Self-Help Book', 'Children Book', 'Magazine'],
        'Health & Beauty': ['Skincare Set', 'Makeup Kit', 'Shampoo', 'Perfume', 'Vitamins', 'Face Mask', 'Hair Dryer'],
        'Toys & Games': ['Board Game', 'Action Figure', 'Puzzle', 'Doll', 'Building Blocks', 'Video Game', 'Toy Car'],
        'Automotive': ['Car Parts', 'Motor Oil', 'Tire', 'Car Accessories', 'GPS Device', 'Car Charger'],
        'Food & Beverages': ['Coffee', 'Tea', 'Snacks', 'Organic Food', 'Energy Drink', 'Chocolate', 'Spices'],
        'Office Supplies': ['Notebook', 'Pen Set', 'Printer Paper', 'Desk Organizer', 'Calculator', 'Stapler']
    }
    
    # Define regions
    regions = ['North America', 'Europe', 'Asia Pacific', 'Latin America', 'Middle East', 'Africa']
    
    # Define payment methods
    payment_methods = ['Credit Card', 'Debit Card', 'PayPal', 'Bank Transfer', 'Cash', 'Digital Wallet']
    
    # Generate data
    data = []
    
    print(f"Generating {num_rows} rows of synthetic data...")
    
    for i in range(num_rows):
        if i % 1000 == 0:
            print(f"Generated {i} rows...")
        
        # Select category and corresponding product
        category = random.choice(categories)
        product = random.choice(products_by_category[category])
        
        # Generate realistic pricing based on category
        price_ranges = {
            'Electronics': (50, 2000),
            'Clothing': (15, 300),
            'Home & Garden': (25, 800),
            'Sports & Outdoors': (20, 500),
            'Books': (10, 80),
            'Health & Beauty': (8, 150),
            'Toys & Games': (12, 200),
            'Automotive': (30, 1000),
            'Food & Beverages': (5, 50),
            'Office Supplies': (3, 100)
        }
        
        min_price, max_price = price_ranges[category]
        unit_price = round(random.uniform(min_price, max_price), 2)
        
        # Generate quantity (most orders are small quantities)
        quantity = np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
                                  p=[0.4, 0.25, 0.15, 0.08, 0.05, 0.03, 0.02, 0.01, 0.005, 0.005])
        
        # Generate order date (last 2 years)
        start_date = datetime.now() - timedelta(days=730)
        end_date = datetime.now()
        order_date = fake.date_between(start_date=start_date, end_date=end_date)
        
        row = {
            'customer_id': f"CUST_{random.randint(1000, 99999)}",
            'product': product,
            'category': category,
            'quantity': quantity,
            'unit_price': unit_price,
            'order_date': order_date,
            'region': random.choice(regions),
            'payment_method': random.choice(payment_methods)
        }
        
        data.append(row)
    
    df = pd.DataFrame(data)
    
    # Add some data quality issues intentionally for the extract phase
    print("Adding intentional data quality issues...")
    
    # 1. Add some missing values (nulls)
    null_indices = np.random.choice(df.index, size=int(0.02 * len(df)), replace=False)
    df.loc[null_indices[:len(null_indices)//3], 'payment_method'] = None
    df.loc[null_indices[len(null_indices)//3:2*len(null_indices)//3], 'region'] = None
    df.loc[null_indices[2*len(null_indices)//3:], 'category'] = None
    
    # 2. Add some duplicates
    duplicate_rows = df.sample(n=int(0.005 * len(df)))
    df = pd.concat([df, duplicate_rows], ignore_index=True)
    
    # 3. Add some inconsistent data types and formatting
    inconsistent_indices = np.random.choice(df.index, size=int(0.01 * len(df)), replace=False)
    df.loc[inconsistent_indices, 'customer_id'] = df.loc[inconsistent_indices, 'customer_id'].str.lower()
    
    # 4. Add some outliers in quantity
    outlier_indices = np.random.choice(df.index, size=int(0.001 * len(df)), replace=False)
    df.loc[outlier_indices, 'quantity'] = np.random.randint(100, 1000, size=len(outlier_indices))
    
    print(f"Dataset generated with {len(df)} total rows (including duplicates)")
    return df

def create_incremental_data(main_df, percentage=0.1):
    """
    Create incremental dataset (recent records)
    
    Args:
        main_df (pandas.DataFrame): Main dataset
        percentage (float): Percentage of data to use as incremental
    
    Returns:
        pandas.DataFrame: Incremental dataset
    """
    # Sort by date and take the most recent records
    df_sorted = main_df.sort_values('order_date', ascending=False)
    incremental_size = int(len(df_sorted) * percentage)
    incremental_df = df_sorted.head(incremental_size).copy()
    
    print(f"Created incremental dataset with {len(incremental_df)} rows")
    return incremental_df

def main():
    """Main function to generate and save datasets"""
    
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    # Generate main dataset
    print("=== Generating Synthetic E-commerce Dataset ===")
    main_dataset = generate_synthetic_data(10000)
    
    # Create incremental dataset
    incremental_dataset = create_incremental_data(main_dataset, 0.15)  # 15% as incremental
    
    # Save datasets
    print("\nSaving datasets...")
    main_dataset.to_csv('data/raw_data.csv', index=False)
    incremental_dataset.to_csv('data/incremental_data.csv', index=False)
    
    # Display summary statistics
    print("\n=== Dataset Summary ===")
    print(f"Main dataset: {len(main_dataset)} rows, {len(main_dataset.columns)} columns")
    print(f"Incremental dataset: {len(incremental_dataset)} rows, {len(incremental_dataset.columns)} columns")
    
    print("\nColumns:", list(main_dataset.columns))
    print("\nData types:")
    print(main_dataset.dtypes)
    
    print("\nFirst few rows of main dataset:")
    print(main_dataset.head())
    
    print("\nDataset saved successfully!")
    print("- Main dataset: data/raw_data.csv")
    print("- Incremental dataset: data/incremental_data.csv")

if __name__ == "__main__":
    main()