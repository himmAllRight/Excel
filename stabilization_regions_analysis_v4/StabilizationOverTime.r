#Input Data
inputArray <- read.delim("graph_data.csv", sep = ",")
#Outputfile
png(file="StabilizationOverTimePlot.png")

#Plot Data
plot(inputArray$time, inputArray$count, type="l", ann=FALSE)

#Regression Line
res=lm(inputArray$count~inputArray$time)
legend(x=20000, y=77, legend="regression")
abline(res, col='red',lwd='3')


#Titles
title(main="Number of Changing Cells Between Time Steps")
title(xlab="Steps", col.lab=rgb(0,0,0))
title(ylab="Changes", col.lab=rgb(0,0,0))

#Legend
legend(x=12000,y=5,legend="lm Regression Line",lwd='3', col='red' )
