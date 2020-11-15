#!/usr/bin/Rscript

#getting file & reading through file line by line

input<-file('stdin', 'r')
#args <- commandArgs(trailingOnly = TRUE)
row <- readLines(input, n=1)

while(length(row)>0) {
	zval=qnorm(as.numeric(row))
	row <- readLines(input, n=1)
}
zval=abs(zval)
write(zval, "")
