# Bond Portfolio Market Risk
I used Python to create a scenario analysis measuring portfolio value flucuations of 100,000 different tenored zero coupon bonds. The underlying data is generated stochastically. I assumed no credit risk and the yield curve steps up by tenor to resemble a normal yield curve. This list of individual bonds is unweighted and assumes a lot size of one for each bond. It contains tenor, yield, an assumed par value of $100, and the calculated bond price, modified duration and convexity. Because I assume a uniform lot size per bond, these bonds are able to be aggregated by tenor to calculate portfolio weights, market value, average yield and total modified duration and convexity.
 
## Raw Data and Portfolio Table
| Bond Tenor | Theoretical Weights | Realized Weights |
| ----------- | ----------- | ----------- |
| 3 | 20% | 19% |
| 5 | 30% | 30% |
| 10 | 30% | 31% |
| 30 | 20% | 20% |
