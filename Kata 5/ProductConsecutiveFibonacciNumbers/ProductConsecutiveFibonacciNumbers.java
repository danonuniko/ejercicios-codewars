/* Kata Level: 5.
 * 
 * The Fibonacci numbers are the numbers in the following integer sequence (Fn):
 * 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...
 * 
 * such as 		F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.
 * 
 * Given a number, say prod (for product), we search two Fibonacci numbers F(n) and F(n+1) verifying	F(n) * F(n+1) = prod.
 * 
 * Your function productFib takes an integer (prod) and returns an array:
 * [F(n), F(n+1), true] or {F(n), F(n+1), 1} or (F(n), F(n+1), True)	depending on the language if F(n) * F(n+1) = prod.
 * 
 * If you don't find two consecutive F(n) verifying F(n) * F(n+1) = prod you will return
 * [F(n), F(n+1), false] or {F(n), F(n+1), 0} or (F(n), F(n+1), False)
 * F(n) being the smallest one such as F(n) * F(n+1) > prod.
 * 
 * Some Examples of Return:		(depend on the language)
 * 
 * productFib(714) # should return (21, 34, true),		# since F(8) = 21, F(9) = 34 and 714 = 21 * 34
 * 
 * productFib(800) # should return (34, 55, false), 	# since F(8) = 21, F(9) = 34, F(10) = 55 and 21 * 34 < 800 < 34 * 55
 * -----
 * productFib(714) # should return [21, 34, true], 
 * productFib(800) # should return [34, 55, false], 
 * -----
 * productFib(714) # should return {21, 34, 1}, 
 * productFib(800) # should return {34, 55, 0},        
 * -----
 * productFib(714) # should return {21, 34, true}, 
 * productFib(800) # should return {34, 55, false}, 
 * Note:
 * You can see examples for your language in "Sample Tests".
 */

public class ProductConsecutiveFibonacciNumbers {

    // Detalle sutil: Si las variables a, b, c las declaro como int en vez de long no superará todos los test por exceso de tiempo (entiendo que se ve obligado a realizar casting en cada iteración y pierde demasiado tiempo).
    public static long[] productFib(long prod) {
        long a = 0 , b = 1 , c = a + b;
        while(prod > b * c) {
            a = b;
            b = c;
            c = a + b; 
        }
        return b * c == prod ? new long[] {b, c, 1} : new long[] {b, c, 0} ;
    }

    public static void main(String[] args) {
        
        long[] result = productFib(714);
        for(long number : result)   System.out.println(number);

        result = productFib(800);
        for(long number : result)   System.out.println(number);

    }

}