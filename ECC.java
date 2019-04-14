import java.io.*;
import java.math.*;
import java.util.*;

public class Ass8
{
    public static long p,q,n,phi,m,d,e,enc,dec;
    public static long GCD(long phi)
    {
        long a,c,b;
        for(long i=4;i<phi;i++)
        {
            a=i;
            b=phi;
            c=b;
            while(b!=0)
            {
                c=b;
                b=a%b;
                a=c;
            }
            if(a==1)
            {
                e=i;
                i=phi;
            }
        }
        return e;
    }
public static long Encryption(long n,long phi,long m)
{
    long x=m,y=m;
    e=GCD(phi);
    for(long a=0;a<e-1;a++)
    {
        x=x*y;
    }
    enc =x%n;
    return enc;
}
public static BigInteger Decryption(long e,long enc,long n,long phi)
{
    BigInteger object2=null;
    try{
        for(long i=1;i<phi;i++)
        {
            if(((i*e)%phi)==1)
            {
                d=i;
                i=phi;
            }
        }
        BigInteger object1=new BigInteger(Long.toString(enc));
        BigInteger object3=new BigInteger(Long.toString(n));
        object1=object1.pow((int)d);
        object2=object1.mod(object3);
    }
    catch(Exception exp)
    {
        System.out.println("Exception in DEC"+e);
    }
    return object2;
}
public static void main(String[] args) {
    Scanner sc=new Scanner(System.in);
    try{
        System.out.println("Enter first prime no");
        p=sc.nextInt();
        System.out.println("Enter second prime no");
        q=sc.nextInt();
        System.out.println("Enter message between 0 to 32");
        m=sc.nextInt();
        n=p*q;
        phi=(p-1)*(q-1);
        enc=Encryption(n, phi, m);
        System.out.println("Encrypt key: "+e);
        System.out.println("Encrypt data: "+enc);
        BigInteger Result=new BigInteger("123");
        Result=Decryption(e,enc,n,phi);
        System.out.println(" Decrypt key: "+d);
        System.out.println("Decrypted data: "+Result.toString());
        }
        catch(Exception exp)
        {
            System.out.println("Exception in main :\n"+e);
        }
        sc.close();
    }
}
/*
OUTPUT
===========OUTPUT 1=============
 
Enter first prime no
17
Enter second prime no
11
Enter message between 0 to 32
11
M is : 11
Encrypt key: 7
Encrypt data: 88
 Decrypt key: 23
Decrypted data: 11
===========OUTPUT 2=============
 
Enter first prime no
17
Enter second prime no
11
Enter message between 0 to 32
11
M is : 11
Encrypt key: 7
Encrypt data: 88
 Decrypt key: 23
Decrypted data: 11

D:\New folder\assn3>java RSA
Enter first prime no
79
Enter second prime no
71
Enter message between 0 to 32
26
M is : 26
Encrypt key: 11
Encrypt data: 1471
 Decrypt key: 3971
Decrypted data: 26


*/
