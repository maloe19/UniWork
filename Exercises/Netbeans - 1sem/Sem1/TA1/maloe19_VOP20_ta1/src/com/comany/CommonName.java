package com.comany;

import java.util.Arrays;
import java.util.Collections;

/**
 * VOP ReEksamen F16
 * Kodeskelet til opgave 4a
 * @author erso
 */
public class CommonName implements Comparable<CommonName>{
    private String name;
    private int girls;
    private int boys;

    public CommonName(String name, int girls, int boys){
        this.name = name;
        this.girls = girls;
        this.boys = boys;
    }

    public String getName() {
        return name;
    }

    public int getTotal(){
        return girls + boys;
    }

    @Override
    public String toString() {
        return String.format("%-12s Girls:%6d Boys:%6d Total:%6d\n", name, girls, boys, getTotal());
    }

    @Override
    public int compareTo(CommonName o) {
        int i = o.girls - this.girls;
        if(i == getTotal()){
            i = o.girls - o.boys;
        }
        throw new UnsupportedOperationException("Not supported yet.");

    }

    public static void main(String[] a){
        //System.out.println("GirlS: " + " Boys " + getTotal());

    }
}
