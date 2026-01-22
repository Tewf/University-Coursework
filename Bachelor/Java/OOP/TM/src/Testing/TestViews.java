package Testing;

public class TestViews {

    public static void main(String[] args) {
        testMapViews();
        System.out.println("---------------");
        testListView();
    }

    private static void testMapViews() {
        // Map source
        java.util.Map<String, Integer> map = new java.util.HashMap<String, Integer>();
        map.put("A", 1);
        map.put("B", 2);

        // VUES (pas des copies)
        java.util.Set<String> keys = map.keySet();
        java.util.Collection<Integer> values = map.values();
        java.util.Set<java.util.Map.Entry<String, Integer>> entries = map.entrySet();

        System.out.println("=== Au début ===");
        System.out.println("map     = " + map);
        System.out.println("keys    = " + keys);
        System.out.println("values  = " + values);
        System.out.println("entries = " + entries);

        // 🔹 1) Modification de la SOURCE
        map.put("C", 3);

        System.out.println("\nAprès map.put(\"C\", 3) :");
        System.out.println("map     = " + map);
        System.out.println("keys    = " + keys);    // C apparait
        System.out.println("values  = " + values);  // 3 apparait
        System.out.println("entries = " + entries); // C=3 apparait

        // 🔹 2) Modification via la VUE keys
        keys.remove("A");

        System.out.println("\nAprès keys.remove(\"A\") :");
        System.out.println("map     = " + map);     // A a disparu
        System.out.println("keys    = " + keys);
        System.out.println("values  = " + values);
        System.out.println("entries = " + entries);

        // 🔹 3) Modification via la VUE entries
        java.util.Iterator<java.util.Map.Entry<String, Integer>> it = entries.iterator();
        if (it.hasNext()) {
            java.util.Map.Entry<String, Integer> e = it.next();
            e.setValue(999); // change la valeur dans la map
        }

        System.out.println("\nAprès modification via entries (setValue(999)) :");
        System.out.println("map     = " + map);
        System.out.println("keys    = " + keys);
        System.out.println("values  = " + values);
        System.out.println("entries = " + entries);
    }

    private static void testListView() {
        java.util.List<Integer> list = new java.util.ArrayList<Integer>();
        list.add(10);
        list.add(20);
        list.add(30);
        list.add(40);

        // subList = VUE sur list (indices 1 inclus, 3 exclus)
        java.util.List<Integer> sub = list.subList(1, 3); // [20, 30]

        System.out.println("=== List / subList ===");
        System.out.println("list = " + list);
        System.out.println("sub  = " + sub);

        // 🔹 1) Modifier la SOURCE
        list.set(1, 99); // change 20 -> 99

        System.out.println("\nAprès list.set(1, 99) :");
        System.out.println("list = " + list); // [10, 99, 30, 40]
        System.out.println("sub  = " + sub);  // [99, 30]

        // 🔹 2) Modifier via la VUE
        sub.set(0, 555); // change l'élément à l'index 1 de list

        System.out.println("\nAprès sub.set(0, 555) :");
        System.out.println("list = " + list); // [10, 555, 30, 40]
        System.out.println("sub  = " + sub);  // [555, 30]
    }
}

