# Zero Coupon Bond Portfolio - Market Risk Analysis
I ran a scenario analysis measuring portfolio value flucuations of 100,000 different tenored zero coupon bonds. The underlying data is generated stochastically. I assumed no credit risk and the yield curve roughly steps up by tenor to resemble a normal yield curve. This list of individual bonds is weighted by tenor and it assumes a lot size of one purchase at par for each bond. It contains tenor, yield, an assumed par value of $100, and the calculated bond price, modified duration and convexity. 

Because I assume a uniform lot size per bond, these bonds are able to be aggregated by tenor to calculate portfolio weights, market value, average yield, modified duration and convexity. Please see the outputs folder for raw data, portfolio aggregation and the final plots.
 
## Raw Data and Portfolio Table
| Bond Tenor | Theoretical Weights | Realized Weights | Market Value | Average Yield | Average Modified Duration | Average Convexity |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| 3 | 10% | 10% | $932,365.34 | 2.50% | 2.93 | 11.42 |
| 5 | 30% | 30% | $2,454,568.25 | 4.00% | 4.81 | 27.74 |
| 10 | 30% | 30% | $1,669,604.53 | 6.00% | 9.43 | 97.9 |
| 20 | 10% | 10% | $218,204.59 | 8.00% | 18.52 | 360.07 |
| 30 | 20% | 20% | $132,170.94 | 9.5% | 27.4 | 775.64 |

## Average Portfolio Yield Curve

![alt text](https://github.com/amason445/bond_portfolio_risk/blob/main/outputs/portfolio_yield_curve.png)

## Portfolio Scenario Test

![alt_text](https://github.com/amason445/bond_portfolio_risk/blob/main/outputs/portfolio_value_change.png)

## References
- [Yield Curves](https://www.investopedia.com/terms/y/yieldcurve.asp)
- [Present Value of a Zero Coupon Bond](https://www.wallstreetprep.com/knowledge/zero-coupon-bond/)
- [Duration and Convexity of a Bond Portfolio](https://analystprep.com/cfa-level-1-exam/fixed-income/duration-and-convexity-of-a-bond-portfolio/)
- [Jorion - FRM Handbook](https://www.google.com/books/edition/Financial_Risk_Manager_Handbook/4ceVmGJSNpcC?hl=en)
