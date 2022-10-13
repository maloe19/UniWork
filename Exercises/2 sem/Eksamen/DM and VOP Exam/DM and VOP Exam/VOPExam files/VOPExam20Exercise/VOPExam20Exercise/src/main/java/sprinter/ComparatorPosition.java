package sprinter;

import java.util.Comparator;

public class ComparatorPosition implements Comparator<Sprinter> {
    @Override
    public int compare(Sprinter o1, Sprinter o2) {
        String i = o1.getoPosition().compareTo(o2.getoPosition());
        if(i==null){
            i = o1.this.getRaceNo()-o2.getRaceNo();
        }
        return i;
    }
}
