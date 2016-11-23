data(iris)
y=iris[,1]
X=as.matrix(iris[,2:4])

lm(y~X)
