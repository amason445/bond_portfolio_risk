# Bond Portfolio Market Risk Analysis
I used Python to create a scenario analysis measuring portfolio value flucuations of 100,000 different tenored zero coupon bonds. The underlying data is generated stochastically. I assumed no credit risk and the yield curve steps up by tenor to resemble a normal yield curve. This list of individual bonds is unweighted and assumes a lot size of one for each bond. It contains tenor, yield, an assumed par value of $100, and the calculated bond price, modified duration and convexity. Because I assume a uniform lot size per bond, these bonds are able to be aggregated by tenor to calculate portfolio weights, market value, average yield and total modified duration and convexity. Please see the outputs folder for raw data, portfolio aggregation and plots.
 
## Raw Data and Portfolio Table
| Bond Tenor | Theoretical Weights | Realized Weights | Market Value | Average Yield 
| ----------- | ----------- | ----------- | ----------- | ----------- |
| 3 | 20% | 19% | $1,755,404.51 | 2.49% |
| 5 | 30% | 30% | $2,385,093.46 | 4.76% |
| 10 | 30% | 31% | $1,558,355.91 | 7.00% |
| 30 | 20% | 20% | $102,230.52 | 10.51% |

## Average Portfolio Yield Curve

![alt text](https://github.com/amason445/bond_portfolio_risk/blob/main/outputs/portfolio_yield_curve.png)

## Portfolio Scenario Test

![alt_text](https://github.com/amason445/bond_portfolio_risk/blob/main/outputs/portfolio_value_change.png)
