import TemperatureApp.*;
import org.omg.CORBA.*;
import java.sql.*;
import java.util.*;
import org.omg.PortableServer.*;

class TemperatureImpl extends TemperatureServicePOA {
    private Connection connection;
    private ORB orb;

    public void setORB(ORB orb_val) {
        orb = orb_val;
    }

    public TemperatureImpl() {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            connection = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/iot_surveillance", "root", "12BRAHIM"
            );
            System.out.println("✅ Connected to MySQL database.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @Override
    public void sendTemperature(String id, String capteur_id, float temperature) {
        try {
            String sql = "INSERT INTO donnee_capteur (id, capteur_id, temperature) VALUES (?,?,?)";
            PreparedStatement stmt = connection.prepareStatement(sql);
            stmt.setString(1, id);
            stmt.setString(2, capteur_id);
            stmt.setFloat(3, temperature);
            stmt.executeUpdate(); // ✅ Execute the insert!

            System.out.println("✅ Data inserted: " + capteur_id + " - " + temperature);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    @Override
    public float[] getLastTemperatures(String id, String capteur_id, int count) {
        float[] result = new float[count];
        Arrays.fill(result, 0); // default to 0
        return result;
    }
}
