""" Scheduler Factory
Hacked together by / Copyright 2021 Ross Wightman
"""
from .cosine_lr import CosineLRScheduler
from .multistep_lr import MultiStepLRScheduler
from .plateau_lr import PlateauLRScheduler
from .poly_lr import PolyLRScheduler
from .step_lr import StepLRScheduler
from .tanh_lr import TanhLRScheduler


def create_scheduler(args, sched, optimizer):
    num_epochs = args.max_epoch

    if getattr(args, 'lr_noise', None) is not None:
        lr_noise = getattr(args, 'lr_noise')
        if isinstance(lr_noise, (list, tuple)):
            noise_range = [n * num_epochs for n in lr_noise]
            if len(noise_range) == 1:
                noise_range = noise_range[0]
        else:
            noise_range = lr_noise * num_epochs
    else:
        noise_range = None
    noise_args = dict(
        noise_range_t=noise_range,
        noise_pct=getattr(args, 'lr_noise_pct', 0.67),
        noise_std=getattr(args, 'lr_noise_std', 1.),
        noise_seed=getattr(args, 'seed', 42),
    )
    cycle_args = dict(
        cycle_mul=getattr(args, 'lr_cycle_mul', 1.),
        cycle_decay=getattr(args, 'lr_cycle_decay', 0.1),
        cycle_limit=getattr(args, 'lr_cycle_limit', 1),
    )
    warmup_lr = getattr(args, 'warmup_lr', 1e-4)
    warmup_epochs = getattr(args, 'warmup_epochs', 5)
    min_lr = getattr(args, 'min_lr', 1e-6)
    cooldown_epochs = getattr(args, 'cooldown_epochs', 0)

    lr_scheduler = None
    if sched == 'cosine':
        lr_scheduler = CosineLRScheduler(
            optimizer,
            t_initial=num_epochs,
            lr_min=min_lr,
            warmup_lr_init=warmup_lr,
            warmup_t=warmup_epochs,
            k_decay=getattr(args, 'lr_k_decay', 1.0),
            **cycle_args,
            **noise_args,
        )
        num_epochs = lr_scheduler.get_cycle_length() + cooldown_epochs
    elif sched == 'tanh':
        lr_scheduler = TanhLRScheduler(
            optimizer,
            t_initial=num_epochs,
            lr_min=min_lr,
            warmup_lr_init=warmup_lr,
            warmup_t=warmup_epochs,
            t_in_epochs=True,
            **cycle_args,
            **noise_args,
        )
        num_epochs = lr_scheduler.get_cycle_length() + cooldown_epochs
    elif sched == 'step':
        lr_scheduler = StepLRScheduler(
            optimizer,
            decay_t=args.decay_epochs,
            decay_rate=args.decay_rate,
            warmup_lr_init=warmup_lr,
            warmup_t=warmup_epochs,
            **noise_args,
        )
    elif sched == 'multistep':
        lr_scheduler = MultiStepLRScheduler(
            optimizer,
            decay_t=args.decay_epochs,
            decay_rate=args.decay_rate,
            warmup_lr_init=warmup_lr,
            warmup_t=warmup_epochs,
            **noise_args,
        )
    elif sched == 'plateau':
        mode = 'min' if 'loss' in getattr(args, 'eval_metric', '') else 'max'
        lr_scheduler = PlateauLRScheduler(
            optimizer,
            decay_rate=args.decay_rate,
            patience_t=args.patience_epochs,
            lr_min=min_lr,
            mode=mode,
            warmup_lr_init=warmup_lr,
            warmup_t=warmup_epochs,
            cooldown_t=0,
            **noise_args,
        )
    elif sched == 'poly':
        lr_scheduler = PolyLRScheduler(
            optimizer,
            power=args.decay_rate,  # overloading 'decay_rate' as polynomial power
            t_initial=num_epochs,
            lr_min=min_lr,
            warmup_lr_init=warmup_lr,
            warmup_t=warmup_epochs,
            k_decay=getattr(args, 'lr_k_decay', 1.0),
            **cycle_args,
            **noise_args,
        )
        num_epochs = lr_scheduler.get_cycle_length() + cooldown_epochs

    return lr_scheduler, num_epochs
