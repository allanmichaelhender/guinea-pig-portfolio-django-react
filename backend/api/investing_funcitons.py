from .models import FtseData, Snp500Data, Nikkei225Data, EuroStoxxData, HsiData
from django.db.models import F, Window
from django.db.models.functions import RowNumber, ExtractYear, ExtractMonth, ExtractQuarter


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


def invest_monthly_quarterly_yearly(
    amount,
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
        for entry in FTSE_queryset:
            FTSE_total_shares += (
                float(amount) / float(entry.close)
            ) * float(FTSE_weight)
            FTSE_value = FTSE_total_shares * float(entry.close)
            total_invested += amount

    if SNP500_queryset is not None and len(SNP500_queryset) != 0:
        for entry in SNP500_queryset:
            SNP500_total_shares += (
                float(amount) / float(entry.close)
            ) * float(SNP500_weight)
            SNP500_value = SNP500_total_shares * float(entry.close)

    if NIKKEI225_queryset is not None and len(NIKKEI225_queryset) != 0:
        for entry in NIKKEI225_queryset:
            NIKKEI225_total_shares += (
                float(amount) / float(entry.close)
            ) * float(NIKKEI225_weight)
            NIKKEI225_value = NIKKEI225_total_shares * float(entry.close)

    if EUROSTOXX_queryset is not None and len(EUROSTOXX_queryset) != 0:
        for entry in EUROSTOXX_queryset:
            EUROSTOXX_total_shares += (
                float(amount) / float(entry.close)
            ) * float(EUROSTOXX_weight)
            EUROSTOXX_value = EUROSTOXX_total_shares * float(entry.close)

    if HSI_queryset is not None and len(HSI_queryset) != 0:
        for entry in HSI_queryset:
            HSI_total_shares += (
                float(amount) / float(entry.close)
            ) * float(HSI_weight)
            HSI_value = HSI_total_shares * float(entry.close)

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
    if frequency == "daily":
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
        HSI_queryset = HsiData.objects.filter(
            date__range=(start_date, end_date)
        ).order_by("date")

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
        FTSE_monthly_queryset = FtseData.objects.annotate(
            row_number=Window(
                expression=RowNumber(),
                partition_by=[ExtractYear("date"), ExtractMonth("date")],
                order_by=F("date").asc(),
            )
        ).filter(row_number=1)

        SNP500_monthly_queryset = Snp500Data.objects.annotate(
            row_number=Window(
                expression=RowNumber(),
                partition_by=[ExtractYear("date"), ExtractMonth("date")],
                order_by=F("date").asc(),
            )
        ).filter(row_number=1)

        NIKKEI225_monthly_queryset = Nikkei225Data.objects.annotate(
            row_number=Window(
                expression=RowNumber(),
                partition_by=[ExtractYear("date"), ExtractMonth("date")],
                order_by=F("date").asc(),
            )
        ).filter(row_number=1)

        EUROSTOXX_monthly_queryset = EuroStoxxData.objects.annotate(
            row_number=Window(
                expression=RowNumber(),
                partition_by=[ExtractYear("date"), ExtractMonth("date")],
                order_by=F("date").asc(),
            )
        ).filter(row_number=1)

        HSI_monthly_queryset = HsiData.objects.annotate(
            row_number=Window(
                expression=RowNumber(),
                partition_by=[ExtractYear("date"), ExtractMonth("date")],
                order_by=F("date").asc(),
            )
        ).filter(row_number=1)

        return invest_monthly_quarterly_yearly(
            amount,
            start_date,
            end_date,
            FTSE_weight,
            SNP500_weight,
            NIKKEI225_weight,
            EUROSTOXX_weight,
            HSI_weight,
            FTSE_monthly_queryset,
            SNP500_monthly_queryset,
            NIKKEI225_monthly_queryset,
            EUROSTOXX_monthly_queryset,
            HSI_monthly_queryset,
        )
    
    elif frequency == "quarterly":
        FTSE_quarterly_queryset = FtseData.objects.annotate(
            row_number=Window(
                expression=RowNumber(),
                partition_by=[ExtractYear("date"), ExtractQuarter("date")],
                order_by=F("date").asc(),
            )
        ).filter(row_number=1)

        SNP500_quarterly_queryset = Snp500Data.objects.annotate(
            row_number=Window(
                expression=RowNumber(),
                partition_by=[ExtractYear("date"), ExtractQuarter("date")],
                order_by=F("date").asc(),
            )
        ).filter(row_number=1)

        NIKKEI225_quarterly_queryset = Nikkei225Data.objects.annotate(
            row_number=Window(
                expression=RowNumber(),
                partition_by=[ExtractYear("date"), ExtractQuarter("date")],
                order_by=F("date").asc(),
            )
        ).filter(row_number=1)

        EUROSTOXX_quarterly_queryset = EuroStoxxData.objects.annotate(
            row_number=Window(
                expression=RowNumber(),
                partition_by=[ExtractYear("date"), ExtractQuarter("date")],
                order_by=F("date").asc(),
            )
        ).filter(row_number=1)

        HSI_quarterly_queryset = HsiData.objects.annotate(
            row_number=Window(
                expression=RowNumber(),
                partition_by=[ExtractYear("date"), ExtractQuarter("date")],
                order_by=F("date").asc(),
            )
        ).filter(row_number=1)

        return invest_monthly_quarterly_yearly(
            amount,
            start_date,
            end_date,
            FTSE_weight,
            SNP500_weight,
            NIKKEI225_weight,
            EUROSTOXX_weight,
            HSI_weight,
            FTSE_quarterly_queryset,
            SNP500_quarterly_queryset,
            NIKKEI225_quarterly_queryset,
            EUROSTOXX_quarterly_queryset,
            HSI_quarterly_queryset,
        )
    
    elif frequency == "yearly":
        FTSE_yearly_queryset = FtseData.objects.annotate(
            row_number=Window(
                expression=RowNumber(),
                partition_by=[ExtractYear("date")],
                order_by=F("date").asc(),
            )
        ).filter(row_number=1)

        SNP500_yearly_queryset = Snp500Data.objects.annotate(
            row_number=Window(
                expression=RowNumber(),
                partition_by=[ExtractYear("date")],
                order_by=F("date").asc(),
            )
        ).filter(row_number=1)

        NIKKEI225_yearly_queryset = Nikkei225Data.objects.annotate(
            row_number=Window(
                expression=RowNumber(),
                partition_by=[ExtractYear("date")],
                order_by=F("date").asc(),
            )
        ).filter(row_number=1)

        EUROSTOXX_yearly_queryset = EuroStoxxData.objects.annotate(
            row_number=Window(
                expression=RowNumber(),
                partition_by=[ExtractYear("date")],
                order_by=F("date").asc(),
            )
        ).filter(row_number=1)

        HSI_yearly_queryset = HsiData.objects.annotate(
            row_number=Window(
                expression=RowNumber(),
                partition_by=[ExtractYear("date")],
                order_by=F("date").asc(),
            )
        ).filter(row_number=1)

        return invest_monthly_quarterly_yearly(
            amount,
            start_date,
            end_date,
            FTSE_weight,
            SNP500_weight,
            NIKKEI225_weight,
            EUROSTOXX_weight,
            HSI_weight,
            FTSE_yearly_queryset,
            SNP500_yearly_queryset,
            NIKKEI225_yearly_queryset,
            EUROSTOXX_yearly_queryset,
            HSI_yearly_queryset,
        )
    

