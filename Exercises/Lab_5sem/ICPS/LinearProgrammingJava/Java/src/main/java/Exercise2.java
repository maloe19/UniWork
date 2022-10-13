import org.ojalgo.OjAlgoUtils;
import org.ojalgo.optimisation.Expression;
import org.ojalgo.optimisation.ExpressionsBasedModel;
import org.ojalgo.optimisation.Optimisation;
import org.ojalgo.optimisation.Variable;

public class Exercise2 {
    public static void main(String[] args)
    {
        ExpressionsBasedModel model = new ExpressionsBasedModel();

        Variable X = model.addVariable("X").weight(-0.4);
        Variable Y = model.addVariable("Y").weight(3.2);

        Expression constraint1 = model.addExpression("Constraint1")
                .upper(5)
                .set(X, 1);

        Expression constraint2 = model.addExpression("Constraint2")
                .upper(7)
                .set(X, 1)
                .set(Y, 1);

        Expression constraint3 = model.addExpression("Constraint3")
                .lower(4)
                .set(X, 1)
                .set(Y, 2);
        
        Expression constraint4 = model.addExpression("Constraint4")
                .upper(5)
                .set(X, -1)
                .set(Y, 1);
                
        Expression constraint5 = model.addExpression("Constraint5")
                .lower(0)
                .set(X, 1);
        
        Expression constraint6 = model.addExpression("Constraint6")
                .lower(0)
                .set(Y, 1);

        Optimisation.Result result = model.maximise();

        System.out.println("Result: " + result);
        System.out.println("Model: " + model);
    }
}
