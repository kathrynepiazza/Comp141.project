#!/usr/bin/Rscript

#getting file & reading through file line by line

input<-file('stdin', 'r')
row <- readLines(input, n=1)
list1=c()

while(length(row)>0) {
	list1=c(as.numeric(row), list1)
	row <- readLines(input, n=1)

}
mean1=mean(list1)
write(mean1, "")
