"""
Example script to load and explore the tall buildings database.

This script demonstrates basic data loading and exploration of the
1000 tall buildings with outer diagrids dataset.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set plotting style
sns.set_style("whitegrid")

def load_database(filepath='../data/database.csv'):
    """Load the database from CSV file."""
    print("Loading database...")
    df = pd.read_csv(filepath)
    print(f"Database loaded successfully!")
    print(f"Shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"Building models: {len(df['GM'].unique())} ground motions")
    return df

def explore_data(df):
    """Print basic information about the dataset."""
    print("\n" + "="*60)
    print("DATASET OVERVIEW")
    print("="*60)
    
    # Design variables
    design_vars = [col for col in df.columns if col.startswith('X')]
    print(f"\nDesign Variables: {len(design_vars)}")
    print(design_vars)
    
    # Ground motions
    print(f"\nGround Motions: {df['GM'].nunique()}")
    print(f"Ground Motion IDs: {sorted(df['GM'].unique())}")
    
    # Key response variables
    response_vars = ['Overall_Max_Drift', 'Max_Displacement', 'Overall_Max_Acc']
    print("\nKey Response Variables:")
    for var in response_vars:
        if var in df.columns:
            print(f"  {var}: min={df[var].min():.4f}, max={df[var].max():.4f}, mean={df[var].mean():.4f}")

def plot_basic_analysis(df):
    """Create basic exploratory plots."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Plot 1: Drift vs Height by Ground Motion
    if 'Overall_Max_Drift' in df.columns and 'Number of stories (Height)' in df.columns:
        sns.scatterplot(data=df, x='Number of stories (Height)', y='Overall_Max_Drift', 
                       hue='GM', ax=axes[0,0], alpha=0.6, palette='tab10')
        axes[0,0].set_title('Maximum Drift vs Building Height')
        axes[0,0].set_xlabel('Number of Stories')
        axes[0,0].set_ylabel('Maximum Inter-storey Drift')
    
    # Plot 2: Drift distribution by Ground Motion
    if 'Overall_Max_Drift' in df.columns:
        df.boxplot(column='Overall_Max_Drift', by='GM', ax=axes[0,1])
        axes[0,1].set_title('Drift Distribution by Ground Motion')
        axes[0,1].set_xlabel('Ground Motion ID')
        axes[0,1].set_ylabel('Maximum Inter-storey Drift')
    
    # Plot 3: Displacement vs Acceleration
    if 'Max_Displacement' in df.columns and 'Overall_Max_Acc' in df.columns:
        sns.scatterplot(data=df, x='Max_Displacement', y='Overall_Max_Acc',
                       hue='GM', ax=axes[1,0], alpha=0.6, palette='tab10')
        axes[1,0].set_title('Displacement vs Acceleration')
        axes[1,0].set_xlabel('Maximum Displacement')
        axes[1,0].set_ylabel('Maximum Acceleration')
    
    # Plot 4: Total Mass vs Height
    if 'TotalMass' in df.columns and 'Number of stories (Height)' in df.columns:
        sns.scatterplot(data=df[df['GM']==1], x='Number of stories (Height)', 
                       y='TotalMass', ax=axes[1,1], alpha=0.6)
        axes[1,1].set_title('Total Mass vs Height (GM 1)')
        axes[1,1].set_xlabel('Number of Stories')
        axes[1,1].set_ylabel('Total Mass (kg)')
    
    plt.tight_layout()
    plt.savefig('exploratory_analysis.png', dpi=300, bbox_inches='tight')
    print("\nPlots saved as 'exploratory_analysis.png'")
    plt.show()

def main():
    """Main function to run the analysis."""
    # Load data
    df = load_database()
    
    # Explore data
    explore_data(df)
    
    # Create plots
    print("\nGenerating exploratory plots...")
    plot_basic_analysis(df)
    
    print("\nAnalysis complete!")

if __name__ == "__main__":
    main()
