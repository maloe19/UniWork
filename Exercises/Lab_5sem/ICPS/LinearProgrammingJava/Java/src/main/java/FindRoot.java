import org.apache.commons.math3.analysis.UnivariateFunction;
import org.apache.commons.math3.analysis.solvers.BisectionSolver;
import java.lang.Math;

public class FindRoot
{
    public static void main(String[] args)
    {
        BisectionSolver solver = new BisectionSolver();
        double result = solver.solve(100, new Function(), 1, 10);
        System.out.println("Result: " + result);
    }

    private static class Function implements UnivariateFunction {
        public double value(double x) { return Math.sin(x);}
    }
}
