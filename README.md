# thriftyCarrot

## Proposal: Grocery Budget App
### Problem
For the frugal, groceries can constitute a big chunk of your spending. However, in budgeting apps, this is represented as one line of spending “Harris Teeters $XX.” While this tells you the amount being spent, it doesn’t tell you if you are spending your money wisely. 75% of this could be snacks and pastries, and only 15% produce, 10% canned goods. It also doesn’t indicate whether your purchases were more effective at one grocery store or another.
Solution: Using our platform, users will be able to leverage the platform to engage in two processes: pre grocery shop planning and post grocery shop analyzing. First, the user writes in the contents of their cart. This can then be used to see if they went to Trader Joes, Haris Teeters or Target how much their cart would cost, and whether or not the product they are looking for is generally sold there. If analyzing their cart, they can see breakdowns of their spending categorically, and potentially other analyses as well.
### Relevance
Grocery spending can be a large black hole in your bank account, and without breaking down your spending by hand it is hard to understand whether or not you are truly shopping in an effective manner. This product would bring ease to the lives of many young adults or even families with children in understanding the efficacy of their grocery spending.
Data management here is vital in order to have relevant and good data on stores and products, as well as using the data entered by users to display as much relevant and useful information for them as possible.
### Initial Plan
For this assignment, we want to first narrow the scope to only grocery stores in Durham. This eliminates the requirement for using a map API, which we could certainly explore as an extra challenge.
Aggregate grocery store data from websites using web scraper such as Selenium. Use Python, Flask, and MySQL to develop the platform.
Designing an efficient database system which allows users to interact with the various relations on goods’ prices.
Implement ways for efficient data updates, which is crucial if we want to dynamically update grocery prices.
Allow users to perform simple data analysis on their own spendings to find potential ways for saving (i.e., cutting down purchase in certain categories or by switching to alternative stores nearby).
### Previous systems
Most apps currently available relating to grocery budgeting are oriented towards offering cashback rewards in return for scanned receipts. In contrast with our proposal, these apps provide rewards for consumption rather than an understanding of the consumption behavior. Examples include Ibotta, Fetch and checkout51
Other apps focus on finding the latest sales and deals at stores near the user. This contrasts with our proposal as well, in that our proposal focuses on enabling the user to make the best decisions based on their preferences, rather than suggesting products to them based on store sales. Examples include coupons.com, shopper, Food on the Table, and Flipp.
Our proposal will be fully user oriented and driven, thus offering a better and more useful experience for users.
