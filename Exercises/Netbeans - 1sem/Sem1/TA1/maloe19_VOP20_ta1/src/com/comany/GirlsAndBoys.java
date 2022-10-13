package com.comany;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;
import java.util.logging.Level;
import java.util.logging.Logger;

/**
 * VOP ReEksamen F16
 * * Kodeskelet til opgave 4b
 * @author erso
 */
public class GirlsAndBoys {

    private Map<String, Integer> girlsMap;
    private Map<String, Integer> boysMap;
    private Set<CommonName> commonSet;

    public GirlsAndBoys() {
        //boysMap = createNameMap(new File("Boys.txt"));
        //girlsMap = createNameMap(new File("Girls.txt"));
    }

    /*
    private Map<String, Integer> createNameMap(File file) {
        throw new UnsupportedOperationException("Not supported yet.");
        Scanner scanner = null;
        try {
            scanner = new Scanner((File) boysMap);
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
            }
        } catch (FileNotFoundException ex) {
            Logger.getLogger(GirlsAndBoys.class.getName()).log(Level.SEVERE, null, ex);
        } finally {
            scanner.close();
        }
        Map<String, Integer> localMap = new HashMap<>();
    }
     */

    public void makeCommonNames() {
        throw new UnsupportedOperationException("Not supported yet.");
        //Collection.sort(commonSet);
    }

    @Override
    public String toString() {
        String st = commonSet.toString();
        st = st.substring(1);
        st = st.substring(0, st.length() - 1);
        st = st.replace(", ", "");
        return st;
    }

    public void sortCommonByName(Comparator<CommonName> comparator) {
        throw new UnsupportedOperationException("Not supported yet.");
    }

    public void write2file(File f) {
        throw new UnsupportedOperationException("Not supported yet.");
    }

    /**
     * @param args the command line arguments
     */

    public static void main(String[] args) {
        GirlsAndBoys gAndB = new GirlsAndBoys();
        gAndB.makeCommonNames();

        System.out.println("Common Names sort by total:\n" + gAndB.toString());
//      gAndB.write2file(new File("CommonSortByNumber.txt"));

        gAndB.sortCommonByName(new CommonNamesComparator());
        System.out.println("Common Names sort by name:\n" + gAndB.toString());
//       gAndB.write2file(new File("CommonSortByName.txt"));
    }

    }
