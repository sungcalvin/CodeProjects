# import yfinance as yf
# data = yf.download('AAPL', start='2019-01-01', end='2025-01-01')
# print(data.head())


#Read Microsoft data and get historical market data
import yfinance as yf
import pandas as pd
import math

#Get historical market data
stock = yf.Ticker("NVDA") 
market = yf.Ticker("VOO") 
hist = stock.history(period="1y")
hist_market = market.history(period="1y")
#print(hist.head())

#Calculate daily returns for stock and market
daily_returns = hist['Close'].pct_change()
daily_returns_market = hist_market['Close'].pct_change()

#Calculate the standard deviation of daily returns for stock and market
std_dev = daily_returns.std()
std_dev_market = daily_returns_market.std()

######  Classes  ######

#Calculate the Sharpe Ratio assuming a risk-free rate of 2% per year and 252 trading days in a year
def calculate_sharpe_ratio(daily_returns, std_dev, rf_rate=0.02, days=252):
    """
    Calculate the Sharpe Ratio.

    Parameters:
    daily_returns (pd.Series): Series of daily returns.
    std_dev (float): Standard deviation of daily returns.
    rf_rate (float): Risk-free rate, default is 0.02.
    days (int): Number of trading days, default is 252.

    Returns:
    float: Sharpe Ratio.
    """
    sharpe_ratio = (daily_returns.mean() - rf_rate) / std_dev * math.sqrt(days)
    return sharpe_ratio

#Calculate the beta of the stock relative to the market
def calculate_beta(daily_returns, daily_returns_market):
    """
    Calculate the beta of the stock relative to the market.

    Parameters:
    daily_returns (pd.Series): Series of daily returns for the stock.
    daily_returns_market (pd.Series): Series of daily returns for the market.

    Returns:
    float: Beta.
    """
    beta = daily_returns.cov(daily_returns_market) / daily_returns_market.var()
    return beta

#Take a list of stock symbols and periods, and return a dataframe of mean, standard deviation, Sharpe ratio, and beta
def summarize_stock_metrics(stocks, market_symbol="VOO", periods = ['3mo', '6mo', '1y', '2y', '5y']):
    """
    Analyze a list of stocks based on historical data.

    Parameters:
    stock_symbols (list): List of stock symbols.
    periods (list): List of periods.

    Returns:
    pd.DataFrame: Dataframe of mean, standard deviation, Sharpe ratio, and beta.
    """
    market = yf.Ticker(market_symbol)
    
    results = []

    for stock_symbol in stocks:
        stock = yf.Ticker(stock_symbol)
        for period in periods:
            hist_market = market.history(period=period)
            daily_returns_market = hist_market['Close'].pct_change()
            
            hist = stock.history(period=period)
            daily_returns = hist['Close'].pct_change()
            std_dev = daily_returns.std()
            sharpe_ratio = calculate_sharpe_ratio(daily_returns, std_dev)
            beta = calculate_beta(daily_returns, daily_returns_market)

            results.append({
                'Stock': stock_symbol,
                'Period': period,
                'Mean': daily_returns.mean(),
                'Sharpe Ratio': sharpe_ratio,
                'Beta': beta
            })
    return pd.DataFrame(results)


# Email the CSV file
def send_email(subject, body, to, attachment):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email.mime.text import MIMEText
    from email import encoders

    from_email = "cs9898@hotmail.com"
    from_password = "@str@P3r@sp#r@"

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(attachment, 'rb').read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="{}"'.format(attachment))
    msg.attach(part)

    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    server.starttls()
    server.login(from_email, from_password)
    server.sendmail(from_email, to, msg.as_string())
    server.quit()

######  Main Code ######

#Define stocks, periods, and market symbol
stocks = ['NVDA', 'COST', 'AAPL', 'VOO']
periods = ['3mo', '6mo', '1y', '2y', '5y']
market_symbol = 'VOO'

#Analyze the results of stocks and print the analysis to a dataframe "results_df" within a csv file
results_df = summarize_stock_metrics(stocks, market_symbol, periods)
csv_file = 'stock_analysis.csv'
results_df.to_csv(csv_file, index=False)
print("Code complete!")
# #Write the DataFrame to a CSV file and send it as an email attachment

# Send the email with the CSV attachment
# send_email(
#     subject="Stock Analysis Report",
#     body="Please find the attached stock analysis report.",
#     to="cs9898@hotmail.com",
#     attachment=csv_file
# )

