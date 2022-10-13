import org.ojalgo.OjAlgoUtils;
import org.ojalgo.optimisation.Expression;
import org.ojalgo.optimisation.ExpressionsBasedModel;
import org.ojalgo.optimisation.Optimisation;
import org.ojalgo.optimisation.Variable;

public class Exercise3 {
    public static void main(String[] args)
    {
        ExpressionsBasedModel model = new ExpressionsBasedModel();

        Variable X = model.addVariable("Gasoline").weight(1.9);
        Variable Y = model.addVariable("Fuel oil").weight(1.5);

        Expression constraint1 = model.addExpression("Constraint1")
                .lower(0)
                .set(X, 1)
                .set(Y, -2);

        Expression constraint2 = model.addExpression("Constraint2")
                .lower(3000000)
                .set(Y, 1);

        Expression constraint3 = model.addExpression("Constraint3")
                .upper(6400000)
                .set(X, 1);

        Expression constraint4 = model.addExpression("Constraint4")
                .lower(0)
                .set(X, 1);
                
        Expression constraint5 = model.addExpression("Constraint5")
                .lower(0)
                .set(X, 1);
        
        Optimisation.Result result = model.maximise();

        System.out.println("Result: " + result);
        System.out.println("Model: " + model);
    }
}
