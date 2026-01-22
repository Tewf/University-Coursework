package TD1;

public class StringBuffer extends Object{
    private char[] lesCaracteres;
    private int n;

    // Constructeurs
    public StringBuffer(int l) {
        if (l < 0) throw new IllegalArgumentException("capacity must be non-negative");
        this.lesCaracteres = new char[l];
        this.n = 0;
    }

    public StringBuffer() {
        this(16);
    }

    public StringBuffer(String str) {
        this(str.length() + 16);
        this.append(str);
    }

    // Méthodes
    public int length() {
        return n;
    }

    public int capacity() {
        return lesCaracteres.length;
    }

    public void ensureCapacity(int capaciteMin) {
        if (capaciteMin < 0) throw new IllegalArgumentException("min capacity must be non-negative");
        if (capaciteMin > lesCaracteres.length) {
            char[] newBuf = new char[Math.max(capaciteMin, lesCaracteres.length * 2 + 2)];
            System.arraycopy(lesCaracteres, 0, newBuf, 0, n);
            lesCaracteres = newBuf;
        }
    }

    public StringBuffer append(String s) {
        if (s == null) throw new NullPointerException("s is null");
        int len = s.length();
        ensureCapacity(n + len);
        for (int i = 0; i < len; i++) {
            lesCaracteres[n++] = s.charAt(i);
        }
        return this;
    }

    public StringBuffer replace(int d, int f, String s) {
     /*int accr=s.length() - (f-d)
    	 *ensurecapacity(n+accr)
    	 *if(accr<0)
    	 *   for(int i=f;i<n;i++) lesCaracteres[i+accr]=lesCaracteres[i]
    	 *else if(accr>0)
    	 *  for(int i=n-1;i>=f;i--) lesCaracteres[i+accr]=lesCaracteres[i]
    	 *for(int i=0;i<s.legnth();i++)
    	 * lesCaracteres[d+i]=s.charAt(i);
    	 *n+=accr
    	 *return this
    	 * 
    	 * */
        if (s == null) throw new NullPointerException("s is null");
        if (d < 0 || f < 0 || d > n || f > n) throw new StringIndexOutOfBoundsException();
        if (d > f) throw new StringIndexOutOfBoundsException();
        delete(d, f);
        insert(d, s);
        return this;
    }

    public StringBuffer delete(int d, int f) {
    	/*return replace(d,f,new String())
    	 * 
    	 * */
        if (d < 0 || f > n || d > f) {
            throw new StringIndexOutOfBoundsException();
        }
        int len = f - d;
        System.arraycopy(lesCaracteres, f, lesCaracteres, d, n - f);
        n -= len;
        return this;
    }

    public StringBuffer insert(int d, String s) {
     /*return replace(d,d,s)
         * 
         * */
        if (s == null) throw new NullPointerException("s is null");
        if (d < 0 || d > n) {
            throw new StringIndexOutOfBoundsException();
        }
        int len = s.length();
        ensureCapacity(n + len);
        System.arraycopy(lesCaracteres, d, lesCaracteres, d + len, n - d);
        for (int i = 0; i < len; i++) {
            lesCaracteres[d + i] = s.charAt(i);
        }
        n += len;
        return this;
    }
}
