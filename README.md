<h1> Neuroscience Data Analysis Beginner Course </h1>


<img src="data_science.png" alt="DataScienceFun">
<p> The following Content is provided for Neuroscientist to get a general overview
about Data-Science and Exploratory Data Analysis using the Python Language from the Medical Univeristy of Innsbruck </p>

The Course is offered in the winter semester, and is conducted by Maximilian Zeidler, Kai Kummer und David Zimmermann

<h2> This course has the following Topics: </h2>

<ul>
  <li> Data Files are located in the Data Folder</li>
  <br>
    <ul> 
      <li> Tabular Data </li>
        <ul>
          <li>Parkinson DataSets </li>
          <li>IV Dataset (iv_condition.csv) </li>
          <li>Calcium Imaging Dataset </li>
         </ul>
      <li> Natural Language Processing </li>
      <li> Signal Processing </li>
      <li> Single Cell Sequencing/Bulk RNA Sequencing </li>
    </ul>
    <br>
  <li> Analysis Script for the Data </li>
  <br>
    <ul>
      <li> Basic Python </li>
      <li> Basic Matplotlib </li>
      <li> Basic Pandas/Numpy </li>
      <li> Basic Clustering </li>
      <li> Basic Dimensional Reduction </li>
      <li> Basic Pandas: Pubmed Analysis </li>
      <li> Basic Tabular: Parkinson Analysis </li>
      <li> Basic Calcium: Calcium Imaging Data Loading </li>
      <li> Single Cell Sequencing Analysis </li>
      <li> Basic PatchClamp: Patch-Clamp Analysis of preprocessed IV Traces </li>
      <li> Games and Fun </li>
     </ul>
     
     
     
<h2> How to set up a virtual enviroment using conda </h2>
<br>
<ul>
<li>First download and install miniconda, add it to your path variable (selecting the checkbox </li>
<li>Open command line in Windows </li>
<li>Type conda to see if everything is functional </li>
</ul>
<br>

The execute the following:

```
# create a new enviroment
conda create -n neurobeginner
conda activate neurobeginner
# check if neurobeginner is at the beginning of your line in the terminal/cmd
conda install -c anaconda ipykernel
python -m ipykernel install --user --name=neurobeginner
conda install pandas
conda install seaborn
conda install matplotlib
```
<br>

Open then Powershell and download the latest file for the scRNA sequencing analysis


```
Invoke-WebRequest https://raw.githubusercontent.com/mouzkolit/NeuroBeginner/main/Scripts/instrcuted_single_cell_analysis.ipynb -OutFile scRNA.ipynb
```
