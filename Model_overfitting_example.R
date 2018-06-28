library(tidyverse)
set.seed(101)
x = runif(60,min = 0, max = 5)
y = 3*x^2 -5*x +20
y
e = rnorm(60,0,5);e

data <- data.frame(x = x,
                  y = y)

plot(data)

data[,"y"] = data[,"y"] + e

train = sample.int(nrow(data), size = 40)
length(train)

data.train = data[train,]
data.test = data[-train,]
dim(data.train)
dim(data.test)


ggplot(data.train) +
  geom_point(aes(x,y))

ggplot(data.test) +
  geom_point(aes(x,y))


?glm()
?lm()
model <- lm(y~x, data = data.train )

summary(model)
#?predict()
#plot(model)

predict(model,data.test)

data.fitted.test <- cbind(data.test, prediction = predict(model, data.test))

data.fitted.train <- cbind(data.train, prediction = predict(model, data.train))

data.fitted.train <- data.fitted.train %>% mutate(residual = prediction - y)
summarize(data.fitted.train, sum_res = sum(residual^2))

data.fitted.test <- data.fitted.test %>% mutate(residual = prediction - y)
summarize(data.fitted.test, sum_res = sum(residual^2))

ggplot(data.fitted.test) +
  geom_point(aes(x= x,y = y, colour = "red")) +
  geom_line(aes(x = x, y = prediction))

ggplot(data.fitted.train) +
  geom_point(aes(x= x,y = y, colour = "red")) +
  geom_line(aes(x = x, y = prediction))


#Model 2
model2 <- lm(y~x + I(x^2), data = data.train )
summary(model2)

data.fitted2.test <- cbind(data.test, prediction = predict(model2, data.test))

data.fitted2.train <- cbind(data.train, prediction = predict(model2, data.train))


data.fitted2.train <- data.fitted2.train %>% mutate(residual = prediction - y)
summarize(data.fitted2.train, sum_res = sum(residual^2))

data.fitted2.test <- data.fitted2.test %>% mutate(residual = prediction - y)
summarize(data.fitted2.test, sum_res = sum(residual^2))

ggplot(data.fitted2.test) +
  geom_point(aes(x= x,y = y, colour = "red")) +
  geom_line(aes(x = x, y = prediction))

ggplot(data.fitted2.train) +
  geom_point(aes(x= x,y = y, colour = "red")) +
  geom_line(aes(x = x, y = prediction))


#Model 3 - overfitting

model3 <- lm(y~ poly(x,20), 
             data = data.train )
summary(model3)

data.fitted3.test <- cbind(data.test, prediction = predict(model3, data.test))

data.fitted3.train <- cbind(data.train, prediction = predict(model3, data.train))

data.fitted3.train <- data.fitted3.train %>% mutate(residual = prediction - y)
summarize(data.fitted3.train, sum_res = sum(residual^2))

data.fitted3.test <- data.fitted3.test %>% mutate(residual = prediction - y)
summarize(data.fitted3.test, sum_res = sum(residual^2))

ggplot(data.fitted3.test) +
  geom_point(aes(x= x,y = y, colour = "red")) +
  geom_line(aes(x = x, y = prediction))

ggplot(data.fitted3.train) +
  geom_point(aes(x= x,y = y, colour = "red")) +
  geom_line(aes(x = x, y = prediction))

model3$coefficients

       
