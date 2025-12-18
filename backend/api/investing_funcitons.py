from .models import FtseData, Snp500Data, Nikkei225Data, EuroStoxxData, HsiData


def invest_daily(
    amount_daily,
    start_date,
    end_date,
    FTSE_weight=0,
    SNP500_weight=0,
    NIKKEI225_weight=0,
    EUROSTOXX_weight=0,
    HSI_weight=0,
    FTSE_queryset=None,
    SNP500_queryset=None,
    NIKKEI225_queryset=None,
    EUROSTOXX_queryset=None,
    HSI_queryset=None,
):
    FTSE_total_shares = 0
    SNP500_total_shares = 0
    NIKKEI225_total_shares = 0
    EUROSTOXX_total_shares = 0
    HSI_total_shares = 0

    FTSE_value = 0
    SNP500_value = 0
    NIKKEI225_value = 0
    EUROSTOXX_value = 0
    HSI_value = 0

    timeframe = end_date - start_date
    total_days = timeframe.days
    total_amount_to_invest = total_days * amount_daily

    if FTSE_queryset is not None and len(FTSE_queryset) != 0:
        FTSE_aggregated_amount_per_day = total_amount_to_invest / (
            len(FTSE_queryset) + 1
        )

        for daily_entry in FTSE_queryset.iterator():
            print(daily_entry)
            FTSE_total_shares += (
                float(FTSE_aggregated_amount_per_day) / float(daily_entry.close)
            ) * float(FTSE_weight)
            FTSE_value = FTSE_total_shares * float(daily_entry.close)

    if SNP500_queryset is not None and len(SNP500_queryset) != 0:
        SNP500_aggregated_amount_per_day = total_amount_to_invest / (
            len(SNP500_queryset) + 1
        )

        for daily_entry in SNP500_queryset:
            SNP500_total_shares += (
                float(SNP500_aggregated_amount_per_day) / float(daily_entry.close)
            ) * float(SNP500_weight)
            SNP500_value = SNP500_total_shares * float(daily_entry.close)

    if NIKKEI225_queryset is not None and len(NIKKEI225_queryset) != 0:
        NIKKEI225_aggregated_amount_per_day = total_amount_to_invest / (
            len(NIKKEI225_queryset) + 1
        )

        for daily_entry in NIKKEI225_queryset:
            NIKKEI225_total_shares += (
                float(NIKKEI225_aggregated_amount_per_day) / float(daily_entry.close)
            ) * float(NIKKEI225_weight)
            NIKKEI225_value = NIKKEI225_total_shares * float(daily_entry.close)

    if EUROSTOXX_queryset is not None and len(EUROSTOXX_queryset) != 0:
        EUROSTOXX_aggregated_amount_per_day = total_amount_to_invest / (
            len(EUROSTOXX_queryset) + 1
        )

        for daily_entry in EUROSTOXX_queryset:
            EUROSTOXX_total_shares += (
                float(EUROSTOXX_aggregated_amount_per_day) / float(daily_entry.close)
            ) * float(EUROSTOXX_weight)
            EUROSTOXX_value = EUROSTOXX_total_shares * float(daily_entry.close)

    if HSI_queryset is not None and len(HSI_queryset) != 0:
        HSI_aggregated_amount_per_day = total_amount_to_invest / (len(HSI_queryset) + 1)

        for daily_entry in HSI_queryset:
            HSI_total_shares += (
                float(HSI_aggregated_amount_per_day) / float(daily_entry.close)
            ) * float(HSI_weight)
            HSI_value = HSI_total_shares * float(daily_entry.close)

    return {
        "total_invested": total_amount_to_invest,
        "end_value": FTSE_value
        + SNP500_value
        + NIKKEI225_value
        + EUROSTOXX_value
        + HSI_value,
    }


def invest_monthly(
    amount_monthly,
    start_date,
    end_date,
    FTSE_weight=0,
    SNP500_weight=0,
    NIKKEI225_weight=0,
    EUROSTOXX_weight=0,
    HSI_weight=0,
    FTSE_queryset=None,
    SNP500_queryset=None,
    NIKKEI225_queryset=None,
    EUROSTOXX_queryset=None,
    HSI_queryset=None,
):
    FTSE_total_shares = 0
    SNP500_total_shares = 0
    NIKKEI225_total_shares = 0
    EUROSTOXX_total_shares = 0
    HSI_total_shares = 0

    FTSE_value = 0
    SNP500_value = 0
    NIKKEI225_value = 0
    EUROSTOXX_value = 0
    HSI_value = 0

    total_invested = 0

    if FTSE_queryset is not None and len(FTSE_queryset) != 0:
        for monthly_entry in FTSE_queryset:
            FTSE_total_shares += (
                float(amount_monthly) / float(monthly_entry.close)
            ) * float(FTSE_weight)
            FTSE_value = FTSE_total_shares * float(monthly_entry.close)
            total_invested += amount_monthly

    if SNP500_queryset is not None and len(SNP500_queryset) != 0:
        for monthly_entry in SNP500_queryset:
            SNP500_total_shares += (
                float(amount_monthly) / float(monthly_entry.close)
            ) * float(SNP500_weight)
            SNP500_value = SNP500_total_shares * float(monthly_entry.close)

    if NIKKEI225_queryset is not None and len(NIKKEI225_queryset) != 0:
        for monthly_entry in NIKKEI225_queryset:
            NIKKEI225_total_shares += (
                float(amount_monthly) / float(monthly_entry.close)
            ) * float(NIKKEI225_weight)
            NIKKEI225_value = NIKKEI225_total_shares * float(monthly_entry.close)

    if EUROSTOXX_queryset is not None and len(EUROSTOXX_queryset) != 0:
        for monthly_entry in EUROSTOXX_queryset:
            EUROSTOXX_total_shares += (
                float(amount_monthly) / float(monthly_entry.close)
            ) * float(EUROSTOXX_weight)
            EUROSTOXX_value = EUROSTOXX_total_shares * float(monthly_entry.close)

    if HSI_queryset is not None and len(HSI_queryset) != 0:
        for monthly_entry in HSI_queryset:
            HSI_total_shares += (
                float(amount_monthly) / float(monthly_entry.close)
            ) * float(HSI_weight)
            HSI_value = HSI_total_shares * float(monthly_entry.close)

    return {
        "total_invested": total_invested,
        "end_value": FTSE_value
        + SNP500_value
        + NIKKEI225_value
        + EUROSTOXX_value
        + HSI_value,
    }


def invest(
    frequency,
    amount,
    start_date,
    end_date,
    FTSE_weight=0,
    SNP500_weight=0,
    NIKKEI225_weight=0,
    EUROSTOXX_weight=0,
    HSI_weight=0,
):
    FTSE_queryset = FtseData.objects.filter(
        date__range=(start_date, end_date)
    ).order_by("date")

    SNP500_queryset = Snp500Data.objects.filter(
        date__range=(start_date, end_date)
    ).order_by("date")

    NIKKEI225_queryset = Nikkei225Data.objects.filter(
        date__range=(start_date, end_date)
    ).order_by("date")

    EUROSTOXX_queryset = EuroStoxxData.objects.filter(
        date__range=(start_date, end_date)
    ).order_by("date")

    HSI_queryset = HsiData.objects.filter(date__range=(start_date, end_date)).order_by(
        "date"
    )

    if frequency == "daily":
        return invest_daily(
            amount,
            start_date,
            end_date,
            FTSE_weight,
            SNP500_weight,
            NIKKEI225_weight,
            EUROSTOXX_weight,
            HSI_weight,
            FTSE_queryset,
            SNP500_queryset,
            NIKKEI225_queryset,
            EUROSTOXX_queryset,
            HSI_queryset,
        )

    elif frequency == "monthly":
        return invest_monthly(
            amount,
            start_date,
            end_date,
            FTSE_weight,
            SNP500_weight,
            NIKKEI225_weight,
            EUROSTOXX_weight,
            HSI_weight,
            FTSE_queryset,
            SNP500_queryset,
            NIKKEI225_queryset,
            EUROSTOXX_queryset,
            HSI_queryset,
        )
