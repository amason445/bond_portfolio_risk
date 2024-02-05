# Zero Coupon Bond Portfolio - Market Risk Analysis
I used Python to create a scenario analysis measuring portfolio value flucuations of 100,000 different tenored zero coupon bonds. The underlying data is generated stochastically. I assumed no credit risk and the yield curve roughly steps up by tenor to resemble a normal yield curve. This list of individual bonds is weighted by tenor and it assumes a lot size of one purchase at par for each bond. It contains tenor, yield, an assumed par value of $100, and the calculated bond price, modified duration and convexity. Because I assume a uniform lot size per bond, these bonds are able to be aggregated by tenor to calculate portfolio weights, market value, average yield, modified duration and convexity. Please see the outputs folder for raw data, portfolio aggregation and the final plots.
 
## Raw Data and Portfolio Table
| Bond Tenor | Theoretical Weights | Realized Weights | Market Value | Average Yield | Average Modified Duration | Average Convexity |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| 3 | 20% | 19% | $1,755,404.51 | 2.49% | 2.93 | 11.42 |
| 5 | 30% | 30% | $2,385,093.46 | 4.76% | 4.77 | 27.34 |
| 10 | 30% | 31% | $1,558,355.91 | 7.00% | 9.35 | 96.09 |
| 30 | 20% | 20% | $102,230.52 | 10.51% | 27.15 | 761.67 |

## Average Portfolio Yield Curve

![alt text](https://github.com/amason445/bond_portfolio_risk/blob/main/outputs/portfolio_yield_curve.png)

## Portfolio Scenario Test

![alt_text](https://github.com/amason445/bond_portfolio_risk/blob/main/outputs/portfolio_value_change.png)

## References
- [Present Value of a Zero Coupon Bond](https://www.wallstreetprep.com/knowledge/zero-coupon-bond/)
- [Jorion - FRM Handbook](https://www.google.com/books/edition/Financial_Risk_Manager_Handbook/4ceVmGJSNpcC?hl=en)
- [Duration and Convexity of a Bond Portfolio](https://analystprep.com/cfa-level-1-exam/fixed-income/duration-and-convexity-of-a-bond-portfolio/)
- [Yield Curves](https://www.investopedia.com/terms/y/yieldcurve.asp)
