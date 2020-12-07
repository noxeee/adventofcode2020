getwd()
setwd("/home/lujza/adventofcode2020/day1")

input <- scan("input.txt", quiet = TRUE)

pairs <- combn(input, 2)

sums <- colSums(pairs)

pos <- match(2020, sums)

print(cumprod(pairs[,pos]))

# part 2

pairs2 <- combn(input, 3)

sums2 <- colSums(pairs2)

pos2 <- match(2020, sums2)

print(cumprod(pairs2[,pos2]))