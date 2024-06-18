# Application of Eigenvalues and Eigenvectors
## Theoretical intro
**Eigenvalue** is associated with a specific linear transformation of a vector space. The main property is that there is some non-zero vector which when multiplied by the scalar is equal to the vector affected by the transformation. Such a vector, therefore, is called an **eigenvector**.
**Eigenvalues can be calculated** from the characteristic polynomial:

<img width="392" alt="image" src="https://github.com/kzholtikova/application-of-eigenvalues-and-eigenvectors/assets/145042018/53a7d137-8014-472b-a9c7-5cac4c19530e">

Then, a linear system with the substituted eigenvalue has to be solved to **find corresponding eigenvectors**.<br>

**Eigenvectors of symmetric matrices** have the following properties:
	1.	Orthogonality of the eigenvectors corresponding to distinct eigenvalues.
	2.	Real Eigenvalues.
	3.	Diagonalizability by an orthogonal matrix.<br><br>

**Principal Component Analysis** is a dimensionality reduction technique that transforms data to a new coordinate system where the greatest variances are on the first coordinates (principal components). **Step-by-Step:**
1. Data Preparation:
	- Start with a dataset having n observations and p variables.
 	- Standardize the data if variables are measured on different scales shifting to the new origin.
2. Covariance Matrix Computation:
	- Calculate the covariance matrix to understand how variables relate to each other by squaring distances from the projected point to the new origin.
4. Eigenvalues and Eigenvectors:
	- Compute the eigenvalues and eigenvectors of the covariance matrix.
	- Eigenvectors determine the directions (principal components), and eigenvalues indicate the magnitude (variance) in these directions.
5. Forming the Principal Components:
	- Rank the eigenvalues from largest to smallest and correspondingly sort the eigenvectors building the best fitting orthogonal line.
	- Choose the top k eigenvectors to form a new feature space - the principal components.
6. Transforming the Data:
	- Multiply the original data by the matrix of top k eigenvectors to transform the data into the new subspace from projections onto PC1 and PC2.
	- The transformed dataset has reduced dimensions but retains most of the variability unless the correlations are far from linear.

PCA have its **drawbacks** though:
- For the computer, it is the dimensionality of the covariance matrix Q = mn*mn. 
- For the user, it is information loss indeed, as PCA reduces dimensionality by projecting data onto a lower-dimensional space. To mitigate it, retain more principal components that capture a higher percentage of the total variance.
- If the features are on different scales, PCA might give more importance to features with larger scales. Before applying PCA, standardize the data to ensure that all variables contribute equally.<br><br>

Overall, **diagonal matrix** is much easier to work with as its powers, exponents, and inverse can be computed straightforwardly. Encryption and decryption becomes more efficient, especially for large matrices, as the complexity of matrix operations is reduced:<br>
_**encrypted = P*D*P^-1 * raw<br>
decrypted = P^-1*D*P * encrypted**_
