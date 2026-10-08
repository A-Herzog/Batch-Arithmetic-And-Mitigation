# Evaluation of mitigation strategies when using batch arrival or batch service in open queueing networks - Supplementary Material

This repository contains supplementary material for the "**Evaluation of mitigation strategies when using batch arrival or batch service in open queueing networks**" report. The scripts in this repository were used to generate the tables and charts in the paper.

## Models

The simulation models can be found in the folders `Models_Base` and `Models_Generated`.

## Results

The statistics results files are located in `Statistics`. The following links direct to the corresponding result diagrams.

### Base models:

* Model 1 (base scenario; bI=1, bS=1..16):
  * [E[W]](images/Model01-EW.png)
  * [E[W] - details](images/Model01-EW-details.png)
  * [E[W] (relative) - details](images/Model01-EWrel-details.png)
  * [Std[W] - details](images/Model01-StdW-details.png)
  * [CV[W] - details](images/Model01-CVW-details.png)
* Model 2 (base scenario; bI=1..4, bS=16):
  * [E[W]](images/Model02-EW.png)
  * [E[W] - details](images/Model02-EW-details.png)
  * [E[W] (relative) - details](images/Model02-EWrel-details.png)
  * [CV[W]](images/Model02-CVW.png)
* Model 3 (batch arithmetic):
  * [E[W] (relative)](images/Model03-EWrel.png)
  * [E[W] (relative) - details](images/Model03-EWrel-details.png)

### State-based:

* Model 4 (state-based; bI=1, bS=12..16):
  * [E[W] (relative)](images/Model04-EWrel.png)
  * [E[W] (relative) - details](images/Model04-EWrel-details.png)
  * [E[W] - details](images/Model04-EW-details.png)
  * [CV[W]](images/Model04-CVW.png)
  * [CV[W] - details](images/Model04-CVW-details.png)
  * [rho - details](images/Model04-rho-details.png)
  * [Batch size frequencies](images/Model04-batch_sizes.png)
* Model 5 (state-based; bI=1..4, bS=12..16):
  * [E[W] - details](images/Model05-EW-details.png)
  * [E[W] (relative)](images/Model05-EWrel.png)
  * [E[W] (relative) - details](images/Model05-EWrel-details.png)
  * [CV[W]](images/Model05-CVW.png)
  * [CV[W] - details](images/Model05-CVW-details.png)
  * [rho - details](images/Model05-rho-details.png)
  * [Batch size frequencies](images/Model05-batch_sizes.png)

### Time-based:

* Model 6 (time-based; last arrival; bI=1, bS=16):
  * [E[W] (relative)](images/Model06-EWrel.png)
  * [E[W] (relative) - details](images/Model06-EWrel-details.png)
  * [CV[W] - details](images/Model06-CVW-details.png)
  * [rho - details](images/Model06-rho-details.png)
  * [Batch size frequencies](images/Model06-batch_sizes.png)
* Model 7 (time-based; last arrival; bI=1..4, bS=16):
  * [E[W] (relative)](images/Model07-EWrel.png)
  * [E[W] (relative) - details](images/Model07-EWrel-details.png)
  * [CV[W] - details](images/Model07-CVW-details.png)
  * [rho - details](images/Model07-rho-details.png)
  * [Batch size frequencies](images/Model07-batch_sizes.png)

### Time+state-based:

* Model 8 (time-based; max waiting time; bI=1, bS=16):
  * [E[W] (relative)](images/Model08-EWrel.png)
  * [E[W] (relative) - details](images/Model08-EWrel-details.png)
  * [CV[W]](images/Model08-CVW.png)
  * [CV[W] - details](images/Model08-CVW-details.png)
  * [rho - details](images/Model08-rho-details.png)
  * [Batch size frequencies](images/Model08-batch_sizes.png)
* Model 9 (time-based; max waiting time; bI=1..4, bS=16):
  * [E[W] (relative)](images/Model09-EWrel.png)
  * [E[W] (relative) - details](images/Model09-EWrel-details.png)
  * [CV[W] - details](images/Model09-CVW-details.png)
  * [rho - details](images/Model09-rho-details.png)
  * [Batch size frequencies](images/Model09-batch_sizes.png)
* Model 10 (time+state-based; last arrival; bI=1, bSmin=12, bSmax=16):
  * [E[W] (relative)](images/Model10-EWrel.png)
  * [E[W] (relative) - details](images/Model10-EWrel-details.png)
  * [CV[W]](images/Model10-CVW.png)
  * [CV[W] - details](images/Model10-CVW-details.png)
  * [rho - details](images/Model10-rho-details.png)
  * [Batch size frequencies](images/Model10-batch_sizes.png)
* Model 11 (time+state-based; last arrival; bI=1..4, bSmin=12, bSmax=16):
  * [E[W] (relative)](images/Model11-EWrel.png)
  * [E[W] (relative) - details](images/Model11-EWrel-details.png)
  * [CV[W] - details](images/Model11-CVW-details.png)
  * [rho - details](images/Model11-rho-details.png)
  * [Batch size frequencies](images/Model11-batch_sizes.png)
* Model 12 (time+state-based; max waiting time; bI=1, bSmin=12, bSmax=16):
  * [E[W] (relative)](images/Model12-EWrel.png)
  * [E[W] (relative) - details](images/Model12-EWrel-details.png)
  * [CV[W]](images/Model12-CVW.png)
  * [CV[W] - details](images/Model12-CVW-details.png)
  * [rho - details](images/Model12-rho-details.png)
  * [Batch size frequencies](images/Model12-batch_sizes.png)
* Model 13 (time+state-based; max waiting time; bI=1..4, bSmin=12, bSmax=16):
  * [E[W] (relative)](images/Model13-EWrel.png)
  * [E[W] (relative) - details](images/Model13-EWrel-details.png)
  * [CV[W] - details](images/Model13-CVW-details.png)
  * [rho - details](images/Model13-rho-details.png)
  * [Batch size frequencies](images/Model13-batch_sizes.png)
* Arrival count comparison:
  * [Arrival count comparison boxplot](images/RunCount-Boxplot.png)

## Simulator

The simulations are carried out using the open source DES [**Warteschlangensimulator**](https://a-herzog.github.io/Warteschlangensimulator/) which has to be downloaded separately.

## Contact

[Alexander Herzog](https://github.com/A-Herzog)

[![Orcid](ORCID-iD_icon_vector.svg) orcid.org/0009-0006-4303-9011](https://orcid.org/0009-0006-4303-9011)
