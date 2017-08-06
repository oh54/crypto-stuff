rm(list=ls())
setwd("/home/oskar/repos/cryptocurrency-experiments/data")

file.names <- dir()
# create a list of dataframes, each csv file corresponds to one dataframe
dfs.list = lapply(file.names, read.csv, header = FALSE)
# inner join/merge the dataframes by v1 (date column)
data.raw = Reduce(function(x, y) merge(x, y, by="V1"), dfs.list)
# remove .csv from file.names and give columns those names (i.e. each column is named by its file)
colnames(data.raw) = c("date-time", Map(function(s) substr(s, 1, nchar(s) - 4), file.names))
rownames(data.raw) = data[, "date-time"]
data.raw = data.raw[, -1]

#x11()
#plot(rownames(data.raw), data.raw[, "market-price"], type = "l")

#X = data.raw[, !colnames(data) %in% c("market-price"), drop = FALSE]
#Y = data.raw[, colnames(data) %in% c("market-price"), drop = TRUE]
#require(randomForest)
#rf <- randomForest(x = X, y = Y, importance = TRUE)
#varImpPlot(rf, type=2, main="Variable importance")

diffs = (data.raw[2:nrow(data.raw), ] / data.raw[1:nrow(data.raw) - 1, ] - 1)

x11()
plot(rownames(diffs)[1600:nrow(diffs)], diffs[1600:nrow(diffs), "market-price"], type = "p")
lines(rownames(diffs)[1600:nrow(diffs)], diffs[1600:nrow(diffs), "market-price"])


ts = diffs[1500:nrow(diffs), "market-price"]


acf(ts, type="correlation", lag.max=40, main="ACF")

par(mfrow = c(1,1))
model1 = arima(ts, order=c(5,0,0), seasonal=list(order=c(0,0,0), period=24))
acf(as.numeric(model1$residuals), type="correlation", lag.max=200, main="ACF")
model1$model