
public class IP {
	public static void main(String[] args) {
		for (int i1=0; i1<args.length; i1+=3) {
			String a = args[i1];
			String b = args[i1+1];
			String c = args[i1+2];
			String aA[] = a.split("\\.");
			String bA[] = b.split("\\.");
			String cA[] = c.split("\\.");

			int flag = 1;
			if(cA.length!=4)
				flag = 2;

			else {
				for (int j=0; j<cA.length; j++) {
					int z = Integer.parseInt(cA[j]);
					if(z<0 || z>255) {
						flag = 2;
						break;
					}
				}
				if(flag !=2) {
					for (int i=0; i<cA.length; i++) {

						int x = Integer.parseInt(aA[i]);  
						int y = Integer.parseInt(bA[i]); 
						int z = Integer.parseInt(cA[i]);


						if (!(z>=x && z<=y)) {
							flag = 0;
							break;

						}
					}
				}
				
				String s1 = "";
				String s2 = "";
				String s3 = "";

				for (int it=0; it<cA.length; it++) {
					s1 = s1 + aA[it];
					s2 = s2 + bA[it];
					s3 = s3 + cA[it];
				}
				long x1 = 0;
				long y1 = 0;
				long z1 = 0;

				x1 = Long.parseLong(s1);
				y1 = Long.parseLong(s2);
				z1 = Long.parseLong(s3);

				if (!(z1>=x1 && z1<=y1)){
					System.out.println("ABC");
					//break;
				} 
				
			}

			
			if (flag == 1)
				System.out.println("InRange");
			else if (flag == 0)
				System.out.println("OutRange");
			else
				System.out.println("InValid");
		}
	}

}
