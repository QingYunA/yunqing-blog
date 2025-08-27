---
title: Diffusion Model Learning
published: 2024-04-22
description: Learning about diffusion models
tags: [diffusion models, learning]
category: Learning
draft: false
---

# Summary of Diffusion Models

## Structure

* A fixed forward noise-adding process
* A U-Net used to learn **how to denoise**

### Noise-Adding Process

**Fixed** is the key to understanding the noise-adding process!

Noise-adding is a fixed process. Given an image, the result of adding noise once and adding noise 100 times is the same (with fixed parameters).

#### How to Obtain Noise?

First, introduce the concept of distribution. We assume the distribution of real images is $q(\mathbf{x}_0)$, and $x_0$ is a real image sampled from $q(\mathbf{x}_0)$.

> You can think of the distribution as a class with 50 students, and the sampled $x_0$ is one student.

The noise-adding process is done step by step. Each step is denoted as $t$, and a total of $T$ noise-adding steps are required.

We obtain noise through a Gaussian distribution. Here, it is important to know that a Gaussian distribution is determined by two parameters: mean and variance, denoted as $\mu$ and $\sigma^2$.
The noise added at step $t$ for an image comes from a Gaussian distribution with mean $\mu_t=\sqrt{1-\beta_t}\mathbf{x_0}$ and variance $\sigma_t^2=\beta_t$. This can be equivalently expressed as: each time, sample an $\epsilon$ from a standard normal distribution, i.e., $\epsilon \sim \mathcal {N}(0, I)$.

#### The Noisy Image at Step $t$, $\mathbf{X}_t$

The image at noise-adding step $t$ is expressed as $\mathbf{x}_t=\sqrt{1-\beta_t}\mathbf{x}_{t-1}+\sqrt{\beta_t}\epsilon$.

Note that $\beta_t$ here is not a constant; it changes with $t$, but follows ($\beta_1<\beta_2<\beta_3<\cdots<\beta_T<1$). It can be linear, binomial, cosine, etc.

The final noisy image $\mathbf{X_T}$ should be pure noise.

### Denoising Process

The denoising process involves step-by-step transforming the noisy result $\mathbf{X_T}$ back to the original image $\mathbf{x_0}$.

What is the purpose of learning this denoising process?
**After obtaining a new noisy image, denoising can generate entirely new images, giving the network the ability to generate on its own.**

We denote this denoising process as $p(x_{t-1}|x_t)$, but this distribution cannot be directly computed. Therefore, we use a neural network to approximate this process, i.e., $p_{\theta}(x_{t-1}|x_t)$, where $\theta$ represents the parameters of the neural network.

### How to Fit the Denoising Process?

Here, we assume that the denoising process also follows a Gaussian distribution. That is, the neural network needs to learn the two parameters mentioned earlier: $\mu_t$ and $\sigma_t^2$. (DDPM fixes the variance and only learns the mean, which has been improved in subsequent papers.)

#### Defining the Objective Function

To drive the neural network to learn the mean during the denoising process, the authors treat the noise-adding process $q$ and the denoising process $p_\theta$ as a VAE (variational auto-encoder). If you are not familiar with VAE, you can skip this part; just know how the final loss function is calculated. (This involves knowledge of KL divergence, ELBO evidence lower bound, and other probability theory concepts. If curious, you can explore each one.)

I haven't fully understood this part yet.

After a series of conditions, a "nice property" is obtained:
$$
q(\mathbf{x_t}|\mathbf{x_0})=\mathcal{N}(\mathbf{x_t};\sqrt{\bar{\alpha_t}},(1-\bar{\alpha_t})\mathbf{I})
$$
where $\alpha_{t}=1-\beta_t$, $\bar{\alpha_t}=\prod_{s=1}^t\alpha_s$.
This property means:

1. Noise can be sampled from a Gaussian distribution, and through appropriate scaling, $\mathbf{x_0}$ can be directly transformed into $\mathbf{x_t}$, where $\bar{\alpha_t}$ can be calculated from the known $\beta_t$.
2. The network predicting the mean can be converted into a network predicting noise.

The final objective function is defined as:
$$\|\epsilon-\epsilon_\theta(\mathbf{x}_t,t)\|^2=\|\epsilon-\epsilon_\theta(\sqrt{\bar{\alpha}_t}\mathbf{x}_0+\sqrt{(1-\bar{\alpha}_t)}\epsilon,t)\|^2$$

### Summary

1. Randomly sample an image $\mathbf{x_0}$ from the real-world data distribution $q(\mathbf{x_0})$.
2. Uniformly sample a noise level $t$ from 1 to $\mathbf{T}$.
3. Sample noise $\epsilon \sim \mathcal{N}(0, I)$ from a Gaussian distribution and corrupt the sampled image $\mathbf{x_0}$ to obtain $\mathbf{x_t}=\sqrt{\bar{\alpha}_t}\mathbf{x}_0+\sqrt{(1-\bar{\alpha}_t)}\epsilon$.
4. The neural network predicts the noise $\epsilon_\theta(\mathbf{x}_t,t)$ based on the corrupted image $\mathbf{x_t}$.