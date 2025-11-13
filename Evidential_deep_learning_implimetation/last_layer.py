import torch
from torch import nn
import torch.nn.functional as F




class Dirichlet(nn.Module):

  def __init__(self,in_features, out_units):

    super().__init__()
    self.dense=nn.Linear(in_features, out_units)
    self.out_units=out_units

  def evidence(self, x):
    return F.softplus(x)

  def forward(self, x):
    out=self.dense(x)
    alpha=self.evidence(out)+1

    return alpha