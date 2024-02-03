# Bond Portfolio Market Risk
I used Python to creat a scenario analysis of measuring portfolio value fluctions of 100,000 different tenored zero coupon bonds. The underlying data is generated stochastically. I assumed no credit risk and the yield curve steps up by tenor and resemble a normal yield curve. The list of individual bonds is unweighted and contains tenor, yield, an assumed par value of $100, and the calculated bond price, modified duration and convexity. Because I assume a uniform lot size of one bond per, these bonds are able to be aggregated by tenor to calculate portfolio weights, market value, average yield and total modified duration and convexity. Finally, a scenario analysis is ran off of this portfolio against changes in yield.
 
