# Application of Eigenvalues and Eigenvectors
## Theoretical intro
**Eigenvalue** is associated with a specific linear transformation of a vector space. The main property is that there is some non-zero vector which when multiplied by the scalar is equal to the vector affected by the transformation. Such a vector, therefore, is called an **eigenvector**.
**Eigenvalues can be calculated** from the characteristic polynomial:

<img width="392" alt="image" src="https://github.com/kzholtikova/application-of-eigenvalues-and-eigenvectors/assets/145042018/53a7d137-8014-472b-a9c7-5cac4c19530e">

Then, a linear system with the substituted eigenvalue has to be solved to **find corresponding eigenvectors**.<br>

**Eigenvectors of symmetric matrices** have the following properties:
	1.	Orthogonality of the eigenvectors corresponding to distinct eigenvalues.
	2.	Real Eigenvalues.
	3.	Diagonalizability by an orthogonal matrix.<br>

Principal Components Analysis have its **drawbacks** though:
- For the computer it is the dimensionality of the covariance matrix Q = mn*mn. 
- For the user it is information loss indeed, as PCA reduces dimensionality by projecting data onto a lower-dimensional space. To mitigate it, retain more principal components that capture a higher percentage of the total variance.
- If the features are on different scales, PCA might give more importance to features with larger scales. Before applying PCA, standardize the data to ensure that all variables contribute equally. <br>

Overall, **diagonal matrix** is much easier to work with as its powers, exponents, and inverse can be computed straightforwardly. Encryption and decryption becomes more efficient, especially for large matrices, as the complexity of matrix operations is reduced:<br>
_**encrypted = P*D*P^-1 * raw<br>
decrypted = P^-1*D*P * encrypted**_
