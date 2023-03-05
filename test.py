from tabulate import tabulate
import pandas as pd

def displayMenu():
    options = {
        'Menu Options': ['1. Generate reports', '2. Modify Members', '3. Modify Providers', '4. Modify Services', '5. Quit']
    }
    df = pd.DataFrame(options)
    df_styled = df.style.set_table_styles([{'selector': 'th', 'props': [('text-align', 'center')]}]).set_properties(**{'text-align': 'left'})
    print(tabulate(df_styled.data, headers=df_styled.columns, tablefmt='fancy_grid', showindex=False))
    return int(input("Please enter your choice: "))

displayMenu()


