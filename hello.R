#!/usr/bin/Rscript

#getting file & reading through file line by line

input<-file('stdin', 'r')
row <- readLines(input, n=1)

while(length(row)>0) {

	    # do something with your row (record)
#	print(row)
	write(row, "")
	row <- readLines(input, n=1)

}

