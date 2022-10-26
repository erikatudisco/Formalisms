fib <- function(nterms) {
  # check if number is great than 0
  if (nterms <= 0) {
    print("Choose a larger number")
  } else if (nterms ==1){
    # check if number is equal to 1
    return(1)
  } else if (nterms ==2){
    # check if number is equal to 2
    return(1)
  } else {
    return(fib(nterms-1)+fib(nterms-2))
  }
 
}
