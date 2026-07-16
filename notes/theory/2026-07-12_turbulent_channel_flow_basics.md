# Turbulent Channel Flow Basics

Date: 2026-07-12

## Purpose

This note summarizes the basic ideas needed for the thesis background on turbulent channel flow. The goal is to understand the flow setup, the important wall quantities, and why these ideas matter before adding temperature, scalar transport, or buoyancy.

Reading targets:

- Stephen B. Pope, `Turbulent Flows`
- Kim, Moin, and Moser, turbulent channel-flow DNS paper
- Any advisor-recommended material already listed in the project notes

## Geometry And Coordinates

A channel flow is the flow between two parallel flat walls. The fluid moves mainly in the streamwise direction between the lower wall and the upper wall.

Common coordinate names:

- `x`: streamwise direction, along the main flow
- `y`: spanwise direction, parallel to the wall and perpendicular to the main flow
- `z`: wall-normal direction, from one wall toward the other

In an ideal channel DNS, the flow is often periodic in `x` and `y`, while the walls are fixed boundaries in `z`.

## No-Slip Condition At The Walls

At a solid wall, the fluid velocity matches the wall velocity. For a stationary wall, this means the velocity is zero at the wall.

This is called the no-slip condition. It is important because it creates strong velocity gradients near the wall. Those gradients produce wall shear stress and generate much of the turbulence structure in wall-bounded flows.

## Mean Flow And Turbulent Fluctuations

In turbulent flow, the velocity changes in space and time. A useful decomposition is:

```text
instantaneous velocity = mean velocity + fluctuation
```

The mean velocity is the averaged part of the flow. The fluctuation is the turbulent part that remains after subtracting the mean.

For channel flow, the mean streamwise velocity is usually strongest near the channel center and zero at the walls. The turbulent fluctuations transport momentum and mix quantities such as temperature or scalar concentration.

## Wall Shear Stress

Wall shear stress is the tangential stress that the fluid applies at the wall. It is related to the velocity gradient at the wall.

Physically, wall shear stress measures how strongly the wall resists the flow. In turbulent channel flow, it is one of the key quantities used to scale the near-wall region.

## Friction Velocity

Friction velocity is a velocity scale built from wall shear stress and density. It is usually written as `u_tau`.

Even though it is called a velocity, it is not the mean flow velocity at a point. It is a scaling quantity that helps compare flows near the wall.

Friction velocity is important because many wall-bounded turbulence quantities are normalized using `u_tau`.

## Friction Reynolds Number

The friction Reynolds number is usually written as `Re_tau`. It compares the channel half-height, friction velocity, and viscosity.

It is a measure of how turbulent and scale-separated the channel flow is. Larger `Re_tau` usually means a wider range between the smallest near-wall scales and the largest outer-flow scales.

For DNS, `Re_tau` strongly affects how fine the grid must be and how expensive the simulation becomes.

## Wall Units

Wall units are normalized variables based on friction velocity and viscosity. They are often marked with a plus sign, such as `z+` or `u+`.

Wall units are useful because the near-wall region has similar structure across many turbulent wall flows when scaled this way.

Examples:

- `z+`: wall-normal distance measured in wall units
- `u+`: mean velocity measured using friction velocity

Using wall units helps judge whether the grid near the wall is fine enough for DNS.

## Near-Wall Regions

The region near the wall is often described using approximate layers:

- Viscous sublayer: very close to the wall, where viscous effects are very strong
- Buffer layer: transition region where viscous effects and turbulence both matter
- Log layer: farther from the wall, where the mean velocity often follows a logarithmic trend in many wall flows
- Outer region: closer to the channel center, where large-scale motions become more important

These regions are not hard boundaries. They are practical descriptions that help interpret profiles and grid requirements.

## Why This Matters For DNS

Direct Numerical Simulation resolves all dynamically important turbulent scales instead of modeling them. This makes DNS accurate but expensive.

For turbulent channel flow, the near-wall region is especially demanding because the smallest scales occur close to the wall. A DNS grid must resolve:

- the sharp velocity gradients at the wall,
- turbulent fluctuations in all three directions,
- near-wall streaks and vortical structures,
- enough time for statistically meaningful averages.

Before adding buoyancy or thermal stratification, it is important to first understand and validate the non-buoyant turbulent channel-flow baseline.

## Connection To Passive Versus Active Scalar Transport

A scalar is a transported quantity such as temperature or concentration.

In passive scalar transport, the scalar is carried and mixed by the flow but does not affect the velocity field. For example, a temperature-like scalar may be solved without adding buoyancy forces.

In active scalar transport, the scalar affects the flow. In this thesis project, temperature can become active if it changes density through the Boussinesq approximation and creates buoyancy forces.

This distinction matters because:

- passive scalar cases help test advection, diffusion, and scalar statistics;
- active thermal cases can change the turbulence itself;
- stable stratification can suppress vertical mixing and modify the channel-flow structure.

## Short Student-Style Summary

Turbulent channel flow is flow between two flat walls. The no-slip condition makes the velocity zero at the walls, which creates strong shear and turbulence near the wall. The flow is usually studied by separating velocity into a mean part and a fluctuating turbulent part.

Wall shear stress gives the friction velocity `u_tau`, and this is used to define wall units and the friction Reynolds number `Re_tau`. These quantities help compare simulations and decide whether the DNS grid is good enough near the wall.

For this thesis, the non-buoyant channel flow is the baseline. After that baseline is understood, temperature or scalar transport can be added. If the scalar is passive, it does not change the flow. If temperature creates buoyancy, it becomes active and can change turbulence, especially in stable stratification.
