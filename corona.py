import os
import numpy as np
import math

# we initialise weights using Xavier initialisation
def SIER(init_t, T, dt, S0, E0, I0, R0, alpha, beta, gamma, rho, N):
    timegrid = np.arange(init_t, T+dt/2, dt)
    t_size = timegrid.size
    S = np.ones(t_size)*S0
    E = np.ones(t_size)*E0
    I = np.ones(t_size)*I0
    R = np.ones(t_size)*R0

    for tt in range(t_size-1):
        S[tt+1] = S[tt] - (rho*beta*S[tt]*E[tt])*dt/N
        E[tt+1] = E[tt] + (rho*beta*S[tt]*E[tt])*dt/N - alpha*E[tt]*dt
        I[tt+1] = I[tt] + alpha*E[tt]*dt - gamma*I[tt]*dt
        R[tt+1] = R[tt] + gamma*I[tt]*dt
        print('{}, {}, {}, {}, {}, {}\n'.format(timegrid[tt+1], 
            S[tt+1], E[tt+1], I[tt+1], R[tt+1], rho))
        # with open(file_log_path, 'a') as f:
        #     f.write('{}, {}, {}, {}, {}, {}\n'.format(timegrid[tt+1], 
        #         S[tt+1], E[tt+1], I[tt+1], R[tt+1], rho))

if __name__ == '__main__':

    ##################
    # Problem setup ##
    ##################
    init_t, T = 0,365
    dt = 1
    timegrid = np.arange(init_t, T+dt/2, dt)
    t_size = timegrid.size
    # data from https://worldpopulationreview.com/countries/malaysia-population/
    N = 32370000
    # data as at 17 Mar
    # total case 566
    # recovered case 42
    # we assume in the 16000 participants,
    # about 500 of them are exposed
    R0 = 42
    E0 = 500
    I0 = 524
    S0 = N - R0 - E0 - I0

    # https://www.medrxiv.org/content/10.1101/2020.03.03.20030858v1.full.pdf+html
    rho = 1
    alpha = 0.143
    beta = 0.25
    gamma = 0.11

    PATH_RESULTS = os.getcwd()
    print(os.getcwd())

    file_log_path = os.path.join(PATH_RESULTS, 'results.txt')
    with open(file_log_path, 'a') as f:
        f.write('time, S, E, I, R, rho\n')
        f.write('{}, {}, {}, {}, {}, {}\n'.format(init_t, S0, E0, I0, R0, rho))

    SIER(init_t, T, dt, S0, E0, I0, R0, alpha, beta, gamma, rho, N)

    rho = 0.5
    with open(file_log_path, 'a') as f:
        f.write('{}, {}, {}, {}, {}, {}\n'.format(init_t, S0, E0, I0, R0, rho))

    SIER(init_t, T, dt, S0, E0, I0, R0, alpha, beta, gamma, rho, N)

    rho = 0.2
    with open(file_log_path, 'a') as f:
        f.write('{}, {}, {}, {}, {}, {}\n'.format(init_t, S0, E0, I0, R0, rho))

    SIER(init_t, T, dt, S0, E0, I0, R0, alpha, beta, gamma, rho, N)
