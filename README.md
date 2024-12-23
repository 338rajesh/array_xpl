# array_xpl: A command line tool for exploring and manipulating arrays

## Reference

### General

* `--key`: list the keys in the npz file
* `--tag`: list the tag in the npz file
* `--verbose`: verbose level

### Manipulations

* `--cat`: Concatenating arrays
* `--stack`: Stacking arrays

### View

* `--summary`: summarize the data
* `--sig_dig`: number of significant digits
* `--print`: print the data
* `--p_bar`: show a progress bar
* `--table_fmt`: Table format, as in `tabulate` python module

### Plotting

* `--plot`: plot the data
* `--line_plot`: plot the data as a line plot
* `--line_plot_opt`: Line plot options
* `--hist1D`: plot the data as a histogram
* `--hist1D_opt`: Histogram plot options
* `--get_frequency`: get the frequency of the data
* `--scatter`: plot the data as a scatter plot
* `--scatter3D`: plot the data as a 3D scatter plot
* `--image_plot`: view the data as images
* `--no_pool`: pool the plots on a single figure
* `--fig_size`: figure size
* `--add_grid`: add a grid
* `--x_label`: x label
* `--y_label`: y label
* `--x_lim`: x limit
* `--y_lim`: y limit
* `--y_log`: y axis in log scale
* `--eq_axs`: equalize the axes
* `--title`: title
* `--no_axs`: no axes
* `--tight_layout`: tight layout

### Transformations

* `--scale`: scale the data
* `--shift`: shift the data

### File Operations

* `--files`: list the files in the directory
* `--merge`: merge the files
* `--append`: 
* `--remove`: a list of keys to be removed from the `*.npz` file
* `--rename`: a pair of keys to be renamed, in the order of source and target

### Save

* `--saveas`: save the data as a file
* `--saveas_json`: save the data as a json file
* `--saveas_dat`: save the data as a text file
* `--log_dir`: log directory

### Evaluations

* `--r2_score`: R^2 score of two arrays
