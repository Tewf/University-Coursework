package TD1;

public class String  extends Object{
	private char[] lesCaracteres;
	
	//Question 1.1
	
	public String() {
		this.lesCaracteres=new char[0];
	}
	
	public String(char[] tab,int d, int f) {
		if (tab == null) throw new NullPointerException("tab is null");
		if (d < 0 || f < 0 || d > tab.length || f > tab.length) throw new IndexOutOfBoundsException("indices out of range");
		if (d > f) throw new IndexOutOfBoundsException("start index greater than end index");
		lesCaracteres=new char[f-d];
		for(int i = d; i < f; i++) {
			this.lesCaracteres[i-d]=tab[i];
		}
	}
	
	public String(String s) {
		this(s.lesCaracteres,0,s.lesCaracteres.length);
	}
	
	//Question 1.2
	
	public char charAt(int i) { 
		if (i < 0 || i >= lesCaracteres.length) throw new IndexOutOfBoundsException("index: " + i);
		return lesCaracteres[i];
	}
	
	public int length() {
		return lesCaracteres.length;
	}
	
	public String substring(int d, int f) {
		if (d < 0 || f < 0 || d > lesCaracteres.length || f > lesCaracteres.length) throw new IndexOutOfBoundsException("indices out of range");
		if (d > f) throw new IndexOutOfBoundsException("start index greater than end index");
		return new String(lesCaracteres,d,f);
	}
	
	public String substring(int d) {
		if (d < 0 || d > lesCaracteres.length) throw new IndexOutOfBoundsException("index out of range");
		return new String(lesCaracteres,d,lesCaracteres.length);
	}
	
	public int compareTo(String s) {
		if (s == null) throw new NullPointerException("s is null");
		int len1 = this.length(), len2 = s.length();
		int lim = Math.min(len1, len2);
      //int lim = len1<len2 ? len1 : len2 ;

        for (int i=0;i<lim;i++) {//for (int i=0;(i<len1)&&(i<len2);i++)
			if (lesCaracteres[i]!=s.charAt(i)){
				return lesCaracteres[i]-s.charAt(i);
			}
		}
	return this.length()-s.length();
	}
	
	 public boolean equals(Object obj) {
     if (this == obj) return true;
     if (!(obj instanceof String)) return false;
     String s = (String) obj;//for old versions
     if (this.length() != s.length()) return false;
     
     return this.compareTo(s)==0;
 }

	public boolean startsWith(String prefixe) {
		if (prefixe == null) throw new NullPointerException("prefixe is null");
		int L= prefixe.length();
		if (L > this.length()) return false;
		String Prefixe= this.substring(0, L);
		return Prefixe.equals(prefixe);
	}
	
	public String concat(String s) {
		if (s == null) throw new NullPointerException("s is null");
		char[] result = new char[this.length() + s.length()];
        
		for(int i=0;i<this.length();i++) {
			result[i]=lesCaracteres[i];
		}
		for(int i=0;i<s.length();i++) {
			result[this.length()+i]=s.charAt(i);
		}
		return new String(result,0,result.length); 
	}
	
	 public int indexOf(char c, int d) {
		 if (d < 0 || d > this.length()) throw new IndexOutOfBoundsException("start index out of range");
		 for(int i=d;i<this.length();i++) {
			 if(this.charAt(i)==c) return i;
		 }
		 return -1;
	 }
	 public int indexOf(char c) {return this.indexOf(c,0);}
	 
	 //Question 1.3
	 public static String valueOf(boolean b) {
		    if (b) {
		        return new String(new char[]{'t','r','u','e'}, 0, 4);
		    } else {
		        return new String(new char[]{'f','a','l','s','e'}, 0, 5);
		    }
		}
	 public static String valueOf(char c) {
	        return new String(new char[]{c}, 0, 1);
	    }
	    
	 public static String valueOf(int i) {
				if (i==-2147483648) {
			return new String(new char[] {'-','2','1','4','7','4','8','3','6','4','8'},0,11);
		}
		    if (i == 0) {
		        return new String(new char[]{'0'}, 0, 1);
		    }
		    boolean neg = i < 0;
		    int num = neg ? -i : i;// if it's the smallest int, -i overflows so construction by hand
		    int digits = (int) Math.log10(num) + 1;
		    int space = digits + (neg ? 1 : 0);// or do 64 biggest possible
		    char[] result = new char[space];
		    int j = space - 1;

		    // fill digits from the end
		    while (num > 0) {
		        result[j] = (char) ('0' + (num % 10));//otherwise it wont be printable;
		        j--;
		        num /= 10;
		    }
		    // leading '-' if needed
		    if (neg) {
		        result[0] = '-';
		    }
		    return new String(result, 0, space);
		}


}
