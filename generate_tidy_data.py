import yfinance as yf
import pandas as pd
import os

def generate_bovespa_dataset():
    tickers = ['VALE3.SA', 'PETR4.SA', 'ITUB4.SA', 'BBDC4.SA', 'ABEV3.SA', 'B3SA3.SA', 'WEGE3.SA', 'MGLU3.SA']
    
    all_data = []
    print("Downloading data from B3...")

    for ticker in tickers:
        try:
            print(f"Fetching {ticker}...")
            df = yf.download(ticker, period="2y", interval="1d", progress=False)
            
            if df.empty:
                continue
                
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.get_level_values(0)
            
            df = df.reset_index()
            df['Ticker'] = ticker.replace('.SA', '')
            all_data.append(df)
        except Exception as e:
            print(f"Error fetching {ticker}: {e}")

    if all_data:
        final_df = pd.concat(all_data, ignore_index=True)
        
        if 'Date' in final_df.columns:
            final_df['Date'] = pd.to_datetime(final_df['Date']).dt.date
        
        cols = ['Ticker'] + [col for col in final_df.columns if col != 'Ticker']
        final_df = final_df[cols]
        
        output_path = 'data/bovespa_tidy.csv'
        final_df.to_csv(output_path, index=False)
        print(f"\nSuccess! Tidy dataset saved to: {output_path}")
        print(f"Total rows: {len(final_df)}")
    else:
        print("\nNo data was downloaded.")

if __name__ == "__main__":
    generate_bovespa_dataset()
