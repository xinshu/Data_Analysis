import java.util.*;

public class hw0{
	private double check = 0.0;
	private ArrayList<Double> posterior(double[] likelihood, double[] prior){
		int len = prior.length;
		double normal = 0.0;
		double[] postarr = new double[len];
		ArrayList<Double> post = new ArrayList<Double>();
		for(int i=0; i<len; i++){
			double tmp = likelihood[i]*prior[i];
			postarr[i] = tmp;
			normal += tmp;
		}
		for(int i=0; i<len; i++){
			postarr[i] /= normal;
			post.add(postarr[i]);
			check += postarr[i];
		}
		return post;
	}
	public static void main(String[] args){
		long starttime = System.currentTimeMillis();//monitor time
		double[] likelihood = {0.5,2,1,3,1,3,2,0.5};
		double[] prior = {0.1,0.3,0.05,0.15,0.05,0.1,0.2,0.05};
		hw0 test = new hw0();
		ArrayList<Double> result = test.posterior(likelihood, prior);
		System.out.println(result);
		System.out.println(test.check);
		
		long finishtime = System.currentTimeMillis();//monitor time
		long elapsetime = finishtime - starttime;
		System.out.println();
		System.out.println("elapsed time: " + elapsetime + "ms");
	}
}