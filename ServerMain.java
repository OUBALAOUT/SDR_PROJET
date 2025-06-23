import org.omg.CORBA.ORB;
import org.omg.PortableServer.POA;
import org.omg.PortableServer.POAHelper;
import org.omg.CosNaming.NamingContextExt;
import org.omg.CosNaming.NamingContextExtHelper;
import org.omg.CosNaming.NameComponent;

public class ServerMain {
    public static void main(String[] args) throws Exception {
        ORB orb = ORB.init(args, null);
        POA rootpoa = POAHelper.narrow(orb.resolve_initial_references("RootPOA"));
        rootpoa.the_POAManager().activate();

        TemperatureImpl tempImpl = new TemperatureImpl();
        org.omg.CORBA.Object ref = rootpoa.servant_to_reference(tempImpl);
        TemperatureApp.TemperatureService href = TemperatureApp.TemperatureServiceHelper.narrow(ref);

        // 🔗 Bind the object in the Naming Service
        org.omg.CORBA.Object objRef = orb.resolve_initial_references("NameService");
        NamingContextExt ncRef = NamingContextExtHelper.narrow(objRef);

        NameComponent path[] = ncRef.to_name("TemperatureService"); // 👈 This name must match client
        ncRef.rebind(path, href);

        System.out.println("Serveur CORBA et HTTP prêts.");

        orb.run();
    }
}
