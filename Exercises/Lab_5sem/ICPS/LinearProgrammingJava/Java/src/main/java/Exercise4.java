import org.ojalgo.OjAlgoUtils;
import org.ojalgo.optimisation.Expression;
import org.ojalgo.optimisation.ExpressionsBasedModel;
import org.ojalgo.optimisation.Optimisation;
import org.ojalgo.optimisation.Variable;

public class Exercise4 {
    public static void main(String[] args)
    {
        ExpressionsBasedModel model = new ExpressionsBasedModel();
        //30x+10y
        Variable X = model.addVariable("Table").weight(30);
        Variable Y = model.addVariable("Chair").weight(10);
        //6x+3y>=40   -   6x+3y<=40
        Expression constraint1 = model.addExpression("Constraint1: Time")
                .upper(40)
                .set(X, 6)
                .set(Y, 3);
        //x+3y<=8   -   y>=3x == -3x+y>=0
        Expression constraint2 = model.addExpression("Constraint2: Customer demand")
                .lower(0)
                .set(X, -3)
                .set(Y, 1);
        //4x+y>=4   -   x+0.25y<=4 eller 4x+y<=16/19
        Expression constraint3 = model.addExpression("Constraint3: Storage space")
                .upper(4)
                .set(X, 1)
                .set(Y, 0.25);
        
        Optimisation.Result result = model.maximise();

        System.out.println("Result: " + result);
        System.out.println("Model: " + model);
    }
}
