# HOI_implementation
Implementation of High Order Interactions 

### Setting up the required packages:

1. Visit the official PyTorch installation guide:
      Go to the PyTorch website and navigate to the "Get Started" page.
      Select your preferences for the following options:
      PyTorch Build: Stable or LTS (long-term support)
      Your Operating System: Linux, Mac, or Windows
      Package: Pip (recommended)
      Language: Python
      Compute Platform: CPU, CUDA 10.2, CUDA 11.1, etc.
2. Get the Installation Command:
      Based on your selections, the PyTorch website will provide the appropriate installation command.
      For example, for the CPU-only version, the command will look like this:
   
        pip install torch==1.8.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
   
      For the GPU version with CUDA 11.1, the command will look like this:

        pip install torch==1.8.1+cu111 -f https://download.pytorch.org/whl/torch_stable.html

3. Install PyTorch:
      Copy and run the command provided by the PyTorch website in your terminal.

4. Install THOI:
      Once PyTorch is installed, install THOI using:

        pip install thoi


### Replicating it on the LLK dataset

Overview of the Chronology: 
        compute the effect sizes -> sort the features according to their effect size -> select the one with the largest effect size as the most representative feature -> that              feature was tested with the Wilcoxon test.


1. Obtain Ketamine and Placebo Dataset from Box
2. Load data (ideally straight from Box)
3. From THOI, run multi_order_measures() on all the datasets and obtain the nplet combinations and info values
4. Compute the delta between two time points for each subject separately (e.g. baseline and 1 hour; but you could do it with all the possible comparisons).
5. Then, you will have a delta for each subject and, in consequence, a distribution of delta values for the placebo and for ketamine.
6. Compute the effect size between the deltas of the two groups.
7. Two steps of comparison: intra-subject comparison (to obtain the difference between two different time points) and then inter-group comparison.
8. Obtain effect sizes for each measure in each band for each timepoint
9. Sort the effect sizes to find the index with the maximum effect size
10. Plot effect sizes for each timepoint, frequency band, and effect size type with nplets on the x axis and effect sizes on the y 
11. Extract the maximum effect values for each frequency band based on the corresponding maximum index for every measure for each subject.
12. Conducted SPSS Mann Whitney on the feature values to obtain group differences in ketamine and midazolam for each frequency band and measure type.
13. Conduct linear mixed modeling and repeated measures anova for exploration
14. Conduct curve fitting to explore timepoint differences in the features.
15. Extract clinical data : MADRS and CADSS. Obtain the 1 hour delta from baseline for CADSS and the 24H delta and Day7 delta from baseline for MADRS
16. Conduct per nplet correlations for the following combinations
                a. HOI subject timepoint 1H: MADRS 24H delta, MADRS Day7delta
                b. HOI subject timepoint 24H: MADRS 24H delta
                c. HOI subject timepoint Day 7: MADRS Day7 delta
17. Also conduct per nplet correlations for the following combinations to assess clinical relevance:
                a. HOI subject timepoint 1H, 24H, and Day7 correlations with MADRS Day7 delta
                b. HOI subject timepoint 1H, 24H, and Day7 correlations with CADSS 1H delta
18. Conduct correlations for the same combinations. However, instead of performing per nplet correlations, correlate only the maximum feature value for the highest effect size index with the clinical data.
19. 
    

Additional Notes:
Selected features were selected according to their effect size. In the case of the correlation with psychometrics, I sorted the features according to their R^2 between the feature and the psychometric measure. This could be done in case you have psychometric scores of depresion, well being, etc.


### Code for communication between local computer and Github

1. Create a local clone onto your computer.
   
2. Adding files on the local computer and syncing that with Github:
      - Enter terminal or bash and set to the working directory
      - `git pull`
      - Add files in the folder
      - `git add <file1> <file2> ... <fileN>` or `git add .` (to add all files to the staging area)
      - `git commit -m "Message of what is being added"`
      - `git push origin main` (if the branch you are working on is different from main, replace the name)

3. Adding files onto Github and syncing that with the local repository
      - Add files onto Github
      - `cd <path to directory>
`Open terminal and set working directory to the clone folder
      - `git pull`
