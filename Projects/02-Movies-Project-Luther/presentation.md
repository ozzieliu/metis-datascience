title: "Project Luther: \nRoger-Ebertron v0.3"
author:
  name: Ozzie Liu
  url: http://ozzieliu.com
output: basic.html
controls: true
--
### Roger-Ebertron v0.3
#### Project Luther

Ozzie Liu  
January 29nd, 2016  
Predicting Roger Ebert's Movie Ratings
--

### Outline

1. Introduction
2. Data / Tools
3. EDA
4. Regression Modeling
5. Summary
6. Next Steps

--
### Movies

"Movies" -> Comic Book Adaptation and Summer Blockbusters

"Film" -> Top 250 movies IMDB

--
### Roger Ebert
<img src="img/ebert.jpg" height="600" align = "middle">

--
### Roger Ebert
Incredibly prolific and influential film critic

**He loved movies**

TV show: Siskel & Ebert

watches 1-2 movies a day over his career


--

### Question

Just like Netflix and Amazon can predict my preferences based on my movie ratings:  
**Can I predict how Mr. Ebert would continue to review movies?**

Even further:  
Create a machine learning algorithm that rates and reviews just as Ebert did?

--
### Challenges - why is this difficult?
He doesn't review like other people - My tastes are very different from his

He is an expert in the domain. He actually understands movies:  
Themes, plot, acting, cinematography

- Probably inadequate to model based on objective data and numbers
- But we'll assume that aggregating movie watchers and critics' ratings can come close.



--
### Data
- 4494 Roger Ebert movie reviews scraped from website over 22 year period 1994-2015
- Metacritic scores
- Rotten Tomatoes critic rating and user rating
- IMDB scores
- Box office sales and production budget

--
### Tools
- iPython Notebook
- Pandas
- BeautifulSoup
- APIs for RottenTomatoes and Metacritic
- OMDB movie database
- Seaborn
- IMDB package in Python

--
### EDA - Distribution

Let's just look at a distribution of his reviews:

<img src="img/hist.png" width = "100%" align = "middle">

--

### EDA - Pair Plot

<img src="img/pair.png" width = "800">


--
### EDA - Correlation with Metacritic
<img src="img/mc.png" weidth = "800">
--

### EDA - Correlation with IMDB

<img src="img/imdb.png" width = "500">
--

### EDA - vs RT User Ratings

<img src="img/rt-user.png" width = "500">

--


### EDA - vs RT Critic Ratings

<img src="img/rt-critic.png" width = "500">


--
### EDA - Genres Distribution

<img src="img/genrehist.png" width = "800">


--

### Regression - First Attempt

Using all the rating features:

<img src="img/ratings.png"  width = "600">

--

### Regression - Add Genre

<img src="img/withgenre.png" width = "700">

--

### Regression - Add Foreign Film Category

<img src="img/foreign.png" width = "700">

--

### Regression - With Cross Validation

<img src="img/cv.png" width = "700">

Mean residual = 0.052
Sum of Squared Residual = 0.34
--
### Regression
<img src="img/formula.png"  width = "800">
--
### Regression Coefficients

<img src="img/coeff.png"  width = "700">
--


### Summary

- Pretty good regression model so far
- Can predict on CV test set within 0.3 stars

Apply to recent movies:
- Star Wars VII: 3.68
- Dirty Grandpa: 0.67
--

### Potential Next Steps

- Collect all his reviews for more data points
- Analyze movie script for sentiment, TF-IDF
- Cluster terms in Mr. Ebert's movie reviews
- Models besides Linear Regression
- Incorporate Box Office & Production Budget



--

### Thanks

ozzie@ozzieliu.com

github.com/ozzieliu/metis-datascience

Questions?
