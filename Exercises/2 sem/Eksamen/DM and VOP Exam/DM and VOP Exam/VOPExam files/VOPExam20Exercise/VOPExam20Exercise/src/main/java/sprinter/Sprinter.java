package sprinter;

import java.util.Set;
import java.util.TreeSet;

public class Sprinter implements Comparable<Sprinter>{

    private int raceNo;
    private int overallPosition;
    private int genderPosition;
    private String country;
    private String officialTime;
    private String halfTime;

    public Sprinter(int raceNo, int overallPosition, int genderPosition, String country, String officialTime, String halfTime) {
        this.raceNo = raceNo;
        this.overallPosition = overallPosition;
        this.genderPosition = genderPosition;
        this.country = country;
        this.officialTime = officialTime;
        this.halfTime = halfTime;
    }

    public int getRaceNo() {
        return raceNo;
    }

    public int getoPosition() {
        return overallPosition;
    }

    public int getGenderPosition() {
        return genderPosition;
    }

    public String getCountry() {
        return country;
    }

    public String getoTime() {
        return officialTime;
    }

    public String gethTime() {
        return halfTime;
    }

        @Override
    public String toString() {
        return String.format("%d \t \t %s \t \t %s \t \t %s \t \t %d \n", getRaceNo(), getCountry(), getoTime(), gethTime(), getoPosition());
    }

    @Override
    public int compareTo(Sprinter o) {
        //TODO
        int i = this.getRaceNo()-o.getRaceNo();
        return i;
    }

    public static void main(String[] args) {
//        Task 1a
        Set<Sprinter> sprinters1 = new TreeSet();
        sprinters1.add(new Sprinter(21080, 1, 1, "Kenya", "2:12:12", "1:04:48"));
       sprinters1.add(new Sprinter(14, 2, 2, "Kenya", "2:12:14", "1:04:48"));
        sprinters1.add(new Sprinter(2, 3, 3, "Ethiopia", "2:12:20", "1:04:49"));
        System.out.println(sprinters1);

//        Task 1b
        Set<Sprinter> sprinters2 = new TreeSet(new ComparatorHalfTime());
        sprinters2.addAll(sprinters1);
       System.out.println(sprinters2);

        Set<Sprinter> sprinters3 = new TreeSet(new ComparatorPosition());
        sprinters3.addAll(sprinters1);
        System.out.println(sprinters3);
    }

}
