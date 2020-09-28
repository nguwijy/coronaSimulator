rm(list = ls())

setwd("C:/Users/nguwijy/Dropbox/Projects/blog/corona_virus/")
data <- read.csv("results.txt", header = T)
data$affected <- data$E + data$I
data$cummulative <- data$E + data$I + data$R

rho_iter <- c(1, 0.5, 0.2)
colors_val <- c("red", "green", "blue", "pink", "yellow")
legend_val <- c("r = 1", "r = 0.5", "r = 0.2")

# jpeg("image.jpg", units="in", width=10, height=11, res=150)
par(mfrow=c(3,1))

for (iter in 1:length(rho_iter)) {
  data_now <- data[data$rho == rho_iter[iter], ]
  plot(data_now$time, data_now$affected, type="l", xlab="Number of Days", ylab="Affected Population (E+I)",
       col = colors_val[iter], main = legend_val[iter])
}
# dev.off()

# jpeg("cumulative.jpg", units="in", width=10, height=11, res=150)
par(mfrow=c(3,1))

for (iter in 1:length(rho_iter)) {
  data_now <- data[data$rho == rho_iter[iter], ]
  plot(data_now$time, data_now$cummulative, type="l", xlab="Number of Days", ylab=" Cumulative (E+I+R)",
       col = colors_val[iter], main = legend_val[iter])
}
# dev.off()