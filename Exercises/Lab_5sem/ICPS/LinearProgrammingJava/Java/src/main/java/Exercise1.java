import org.ojalgo.OjAlgoUtils;
import org.ojalgo.optimisation.Expression;
import org.ojalgo.optimisation.ExpressionsBasedModel;
import org.ojalgo.optimisation.Optimisation;
import org.ojalgo.optimisation.Variable;

public class Exercise1 {
    public static void main(String[] args)
    {
        ExpressionsBasedModel model = new ExpressionsBasedModel();

        Variable X = model.addVariable("X").weight(3);
        Variable Y = model.addVariable("Y").weight(4);

        Expression constraint1 = model.addExpression("Constraint1")
                .upper(14)
                .set(X, 1)
                .set(Y, 2);

        Expression constraint2 = model.addExpression("Constraint2")
                .upper(0)
                .set(X, 3)
                .set(Y, -1);

        Expression constraint3 = model.addExpression("Constraint3")
                .upper(2)
                .set(X, 1)
                .set(Y, -1);

        Optimisation.Result result = model.maximise();

        System.out.println("Result: " + result);
        System.out.println("Model: " + model);
    }
}
